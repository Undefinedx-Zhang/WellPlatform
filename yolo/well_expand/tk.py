import tkinter as tk
from PIL import Image, ImageTk

# 创建主应用程序窗口
root = tk.Tk()
root.title("显示图片")

# 打开本地图片
image_path = r"/original_dataset/manhole_cover/train/broke/well1_0001.jpg"
image = Image.open(image_path)

# 将图片转换为Tkinter的PhotoImage对象
tk_image = ImageTk.PhotoImage(image)

# 创建标签组件并显示图片
label = tk.Label(root, image=tk_image)
label.pack()

# 运行Tkinter事件循环
root.mainloop()
