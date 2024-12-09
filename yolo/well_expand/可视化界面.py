import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
from ultralytics import YOLO
# 执行目标检测并显示结果的函数
def detect_objects():
    # 执行目标检测
    results = model(selected_image_path.get())

    # 获取原始图像
    original_image = Image.open(selected_image_path.get())
    draw = ImageDraw.Draw(original_image)

    # 类别映射
    class_mapping = {0: 'Good', 1: 'Break', 2: 'Lose', 3: 'Uncovered', 4: 'Circle'}

    # 字体设置
    font = ImageFont.truetype("arial.ttf", 25)

    # 绘制边界框
    conf, cls_idx = results[0].boxes.data.tolist()[0][-2:]
    boxes = results[0].boxes.xyxy.tolist()
    for box in boxes:
        x1, y1, x2, y2 = box
        # 在图像上绘制边界框
        draw.rectangle([x1, y1, x2, y2], outline='yellow', width=4)
        # 在边界框上标注置信度和类别信息
        label = f'{class_mapping[int(cls_idx)]} {conf:.2f}'
        print(f'{class_mapping[int(cls_idx)]} {conf:.2f}')
        draw.text((x1, y1), label, fill='blue', font=font)

    # 显示检测后的图像
    original_image = original_image.resize((400, 400))
    tk_image = ImageTk.PhotoImage(original_image)
    selected_image_label.configure(image=tk_image)
    selected_image_label.image = tk_image
# 选择图片文件的函数
def select_image():
    file_path = filedialog.askopenfilename(title="选择一张图片", filetypes=[("图片文件", "*.jpg;*.png;*.jpeg")])
    if file_path:
        selected_image_path.set(file_path)
        # 显示选定的图片
        selected_image = Image.open(file_path)
        selected_image = selected_image.resize((400, 400))
        tk_image = ImageTk.PhotoImage(selected_image)
        selected_image_label.configure(image=tk_image)
        selected_image_label.image = tk_image

# 创建主应用程序窗口
root = tk.Tk()
root.title("目标检测")
root.geometry("450x500")

# 选定的图片路径变量
selected_image_path = tk.StringVar()

# 加载YOLO模型
model = YOLO('../best.pt')

# 创建“选择图片”按钮
select_button = tk.Button(root, text="选择图片", command=select_image, width=15, height=2)
select_button.place(x=50, y=430)

# 创建“检测目标”按钮
detect_button = tk.Button(root, text="检测目标", command=detect_objects, width=15, height=2)
detect_button.place(x=300, y=430)

# 图片标签
selected_image_label = tk.Label(root)
selected_image_label.place(x=20, y=20)

image_label = tk.Label(root)
image_label.place(x=450, y=20)

# 运行Tkinter事件循环
root.mainloop()
