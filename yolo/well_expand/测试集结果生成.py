import os
import re
import tqdm
from PIL import Image
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
def numerical_sort(value):
    """
    使用正则表达式从文件名中提取数字，并将其转换为整数进行排序。
    """
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    #print(parts)
    parts[1::2] = map(int, parts[1::2])
    return parts
if __name__ == '__main__':

    # 加载模型
    model = YOLO(r'D:\project_and_code\ultralytics-main\runs\detect\train1\weights\best.pt')
    root="../test_data/2024服创大赛A03井盖数据完整/井盖测试集/测试集图片"
    file_list = os.listdir("../test_data/2024服创大赛A03井盖数据完整/井盖测试集/测试集图片")
    file_list.sort(key=numerical_sort)
    count=0

    # 使用 tqdm 创建进度条迭代器
    for image_path in tqdm.tqdm(file_list):
        count += 1
        # 预测
        results = model(os.path.join(root,image_path))
        for index in range(len(results[0].boxes.data.tolist())):
            conf, cls_idx = results[0].boxes.data.tolist()[index][-2:]
            boxes = results[0].boxes.xyxy[index].tolist()
            x1, y1, x2, y2 = boxes
            with open("../res1.txt", "a") as file:
                file.write(f"{image_path.split('/')[-1]}  {int(cls_idx)}  {conf}  {int(x1+0.5)}  {int(y1+0.5)}  {int(x2+0.5)}  {int(y2+0.5)}\n")
