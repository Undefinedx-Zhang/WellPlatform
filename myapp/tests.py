from django.test import TestCase

# Create your tests here.
from PIL import Image
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
class MyTest(TestCase):
    def test_example(self):
        # 加载模型
        model = YOLO("../yolo/runs/detect/train1/weights/best.pt")
# 图片路径
        image_path = r"../static/pics/1.jpg"
# 预测
        results = model(image_path)
# 获取原始图像
        original_image = Image.open(image_path)
        draw = ImageDraw.Draw(original_image)
# 标签映射
        class_mapping = {0: "完好", 1: "破损", 2: "丢失", 3: "未覆盖", 4: "井圈问题"}
# 字体设置
        font = ImageFont.truetype("arial.ttf", 20)
# 绘制边界框
        conf, cls_idx = results[0].boxes.data.tolist()[0][-2:]
        boxes = results[0].boxes.xyxy.tolist()
        for box in boxes:
            x1, y1, x2, y2 = box
    # 在图像上绘制边界框
            draw.rectangle([x1, y1, x2, y2], outline="yellow", width=4)
    # 在边界框上标注置信度和类别信息
            label = f"{class_mapping[int(cls_idx)]} {conf:.2f}"
            draw.text((x1, y1 - 21), label, fill="blue", font=font)
    # 把draw保存一下图像文件
            save_path = r"../static/save/1.jpg"
            original_image.save(save_path)
# 显示绘制后的图像
#original_image.show()
