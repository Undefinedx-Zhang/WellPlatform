from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.test.runner import DiscoverRunner
import os
from django.contrib import messages
from django.shortcuts import redirect
# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.test import TestCase
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO


# Create your views here.
def index(request):
    return render(request,"index.html")

def map(request):
    return render(request,"map.html")

def carContrl(request):
    return render(request,"carContrl.html")

def message(request):
    return render(request,"message.html")

def static1(request):
    return render(request,"static.html")
def table1(request):
    return render(request,"table1.html")

def table2(request):
    return render(request,"table2.html")

def tail_more(request):
    return render(request,"tail_more.html")
# Create your views here.
def upload(request):
    return render(request, 'upload.html')

def tail_sm(request):
    return render(request, 'tail_sm.html')

def table(request):
    return render(request, 'table.html')


#执行文件上传处理
from django.shortcuts import redirect
from django.contrib import messages
from PIL import Image
import os
from io import BytesIO
import os
import time
from io import BytesIO
from PIL import Image
from django.contrib import messages
from django.shortcuts import redirect

from django.http import JsonResponse

def doupload(request):
    # 生成新文件名，使用时间戳
    filename = f"{int(time.time())}.jpg"
    myfile = request.FILES.get("pic", None)
    if myfile is not None:
        # 生成上传后的文件路径
        upload_path = os.path.join("./static/pics/", filename)
        # 使用内存中的文件进行处理
        img = Image.open(myfile)
        img = img.convert("RGB")  # 确保图像格式为RGB
        # 使用BytesIO保存压缩后的图像
        buffer = BytesIO()
        img.save(buffer, "JPEG", quality=80)
        buffer.seek(0)
        # 将压缩后的图像保存到目标路径
        with open(upload_path, "wb") as destination:
            destination.write(buffer.getvalue())
        # 将文件名存储在会话中
        request.session['uploaded_filename'] = filename
        # 返回文件名和路径
        response_data = {
            'uploaded_image_url': f"/static/pics/{filename}",
            'filename': filename
        }
        return JsonResponse(response_data)
    else:
        messages.error(request, "未选择文件。")
        return redirect(request.META.get('HTTP_REFERER'))



@csrf_exempt
def run_test(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        filename = data.get('filename')
        if not filename:
            return JsonResponse({'status': 'failed', 'message': 'No filename provided.'})

        # 加载模型
        model = YOLO("../yolo/runs/detect/train1/weights/best.pt")

        image_path = os.path.join(r"E:\pythonProject\djangoProject1\static\pics", filename)

        # 预测
        results = model(image_path)
        # 获取原始图像
        original_image = Image.open(image_path)
        draw = ImageDraw.Draw(original_image)
        # 标签映射
        class_mapping = {0: "Good", 1: "Broke", 2: "Lose", 3: "Uncovered", 4: "Circle"}
        # 字体设置为相对大小
        font_size = min(original_image.size) // 20
        # 字体设置
        font = ImageFont.truetype("arial.ttf", font_size)
        # 存储所有检测到的对象的标签和置信度
        labels = []
        # 绘制边界框
        for result in results:
            conf, cls_idx = result.boxes.data.tolist()[0][-2:]
            boxes = result.boxes.xyxy.tolist()
            for box in boxes:
                x1, y1, x2, y2 = box
                # 在图像上绘制边界框
                draw.rectangle([x1, y1, x2, y2], outline="yellow", width=4)
                # 在边界框上标注置信度和类别信息
                label = f"{class_mapping[int(cls_idx)]} {conf:.2f}"
                draw.text((x1, y1 - 21), label, fill="blue", font=font)
                labels.append({'class': class_mapping[int(cls_idx)], 'confidence': conf, 'bbox': [x1, y1, x2, y2]})

        # 将图像压缩后保存
        buffer = BytesIO()
        original_image.save(buffer, "JPEG", quality=90)
        buffer.seek(0)

        # 将压缩后的图像保存到文件
        save_path = os.path.join(r"E:\pythonProject\djangoProject1\static\save", filename)
        with open(save_path, "wb") as f:
            f.write(buffer.getvalue())

        return JsonResponse({'status': 'success', 'save_path': f"/static/save/{filename}", 'labels': labels})

    return JsonResponse({'status': 'failed'})

# 上传和删除数据
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_case_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id=data.get('itemId')
            item_name = data.get('itemName')
            responsible_dept = data.get('responsibleDept')
            upload_date = data.get('uploadDate')
            new_entry = {
                "id": item_id,
                "check": "",
                "name": item_name,
                "part": responsible_dept,
                "time": upload_date,
                "oper": ""
            }
            with open('./static/json/case.json', 'r+', encoding='utf-8') as file:
                file_data = json.load(file)
                file_data['data'].append(new_entry)
                file.seek(0)
                json.dump(file_data, file, ensure_ascii=False, indent=4)
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def delete_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        # 读取现有的 case.json 文件
        with open('./static/json/case.json', 'r', encoding='utf-8') as file:
            cases = json.load(file)

        # 找到并删除指定的条目
        cases['data'] = [case for case in cases['data'] if case['id'] != item_id]

        # 将更新后的数据写回 case.json 文件
        with open('./static/json/case.json', 'w', encoding='utf-8') as file:
            json.dump(cases, file, ensure_ascii=False, indent=4)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)


