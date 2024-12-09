import math, time
from itertools import chain
import torch
import torch.nn.functional as F
from torch import nn
from base import BaseModel
from utils.helpers import set_trainable
from utils.losses import *
from models.decoders import *
from models.encoder import Encoder
from utils.losses import CE_loss


class Consistency_ResNet50_CD(BaseModel):
    def __init__(self, num_classes, conf, sup_loss=None, cons_w_unsup=None, testing=False,
                 pretrained=True, use_weak_lables=False, weakly_loss_w=0.4):

        self.num_classes = num_classes
        if not testing:
            assert (sup_loss is not None) and (cons_w_unsup is not None)

        super(Consistency_ResNet50_CD, self).__init__()
        assert int(conf['supervised']) + int(conf['semi']) == 1, 'one mode only'
        if conf['supervised']:
            self.mode = 'supervised'
        else:
            self.mode = 'semi'
        # Supervised and unsupervised losses
        if conf['un_loss'] == "KL":
            self.unsuper_loss = softmax_kl_loss
        elif conf['un_loss'] == "MSE":
            self.unsuper_loss = softmax_mse_loss
        elif conf['un_loss'] == "JS":
            self.unsuper_loss = softmax_js_loss
        else:
            raise ValueError(f"Invalid supervised loss {conf['un_loss']}")

        self.unsup_loss_w = cons_w_unsup
        self.sup_loss_w = conf['supervised_w']
        self.softmax_temp = conf['softmax_temp']
        self.sup_loss = sup_loss
        self.sup_type = conf['sup_loss']

        # Use weak labels
        self.use_weak_lables = use_weak_lables
        self.weakly_loss_w = weakly_loss_w
        # pair wise loss (sup mat)
        self.aux_constraint = conf['aux_constraint']
        self.aux_constraint_w = conf['aux_constraint_w']
        # confidence masking (sup mat)
        self.confidence_th = conf['confidence_th']
        self.confidence_masking = conf['confidence_masking']

        # Create the model
        self.encoder = Encoder(pretrained=pretrained)

        # The main encoder
        upscale = 8
        num_out_ch = 2048
        decoder_in_ch = num_out_ch // 4
        self.main_decoder = MainDecoder(upscale, decoder_in_ch, num_classes=num_classes)

        # The auxilary decoders
        if self.mode == 'semi' or self.mode == 'weakly_semi':
            vat_decoder = [VATDecoder(upscale, decoder_in_ch, num_classes, xi=conf['xi'],
                                      eps=conf['eps']) for _ in range(conf['vat'])]
            drop_decoder = [DropOutDecoder(upscale, decoder_in_ch, num_classes,
                                           drop_rate=conf['drop_rate'], spatial_dropout=conf['spatial'])
                            for _ in range(conf['drop'])]
            cut_decoder = [CutOutDecoder(upscale, decoder_in_ch, num_classes, erase=conf['erase'])
                           for _ in range(conf['cutout'])]
            context_m_decoder = [ContextMaskingDecoder(upscale, decoder_in_ch, num_classes)
                                 for _ in range(conf['context_masking'])]
            object_masking = [ObjectMaskingDecoder(upscale, decoder_in_ch, num_classes)
                              for _ in range(conf['object_masking'])]
            feature_drop = [FeatureDropDecoder(upscale, decoder_in_ch, num_classes)
                            for _ in range(conf['feature_drop'])]
            feature_noise = [FeatureNoiseDecoder(upscale, decoder_in_ch, num_classes,
                                                 uniform_range=conf['uniform_range'])
                             for _ in range(conf['feature_noise'])]

            self.aux_decoders = nn.ModuleList([*vat_decoder, *drop_decoder, *cut_decoder,
                                               *context_m_decoder, *object_masking, *feature_drop, *feature_noise])

    def forward(self, A_l=None, B_l=None, target_l=None, A_ul=None, B_ul=None,s_A_ul=None,s_B_ul=None, curr_iter=None,epoch=None):
        if not self.training:
            return self.Yolo(A_l, B_l)
        #sup phase
        output_l = self.Yolo(A_l, B_l)
        loss_sup=self.sup_loss(output_l,target_l)
        #unsup phase
        output_Weak_ul=self.Yolo(A_ul,B_ul)
        output_Strong_ul=self.Yolo(s_A_ul,s_B_ul)
        loss_unsup=self.unsup_loss(output_Weak_ul,output_Strong_ul)
        curr_losses = {'loss_sup': loss_sup}
        #time coefficient
        weight_u = self.unsup_loss_w(epoch=epoch, curr_iter=curr_iter)
        loss_unsup = loss_unsup * weight_u
        curr_losses['loss_unsup'] = loss_unsup
        total_loss = loss_unsup + loss_sup
        return total_loss, curr_losses

    def get_backbone_params(self):
        return self.encoder.get_backbone_params()

    def get_other_params(self):
        if self.mode == 'semi':
            return chain(self.encoder.get_module_params(), self.main_decoder.parameters(),
                         self.aux_decoders.parameters())

        return chain(self.encoder.get_module_params(), self.main_decoder.parameters())

