import shutil
import os

a_path = "./img1"
b_path = r"E:\sci_file\otherProject\efficientteacher-main\datasets\zdj\images\wbq1"
with open("cnt", "r") as f:
    lines = f.readlines()  # 读取文件的所有行，返回一个包含每行内容的列表
    last_line = lines[-1].strip()  # 获取最后一行内容，并去除首尾空白字符（如换行符等）
    try:
        num = int(last_line)  # 尝试将最后一行内容转换为整数
    except ValueError:
        print("最后一行内容无法转换为整数")
index = num
cnt1=0
for root, dirs, files in os.walk(a_path):
    for file in files[index:]:
        if file.endswith(".jpg") or file.endswith(".png"):
            cnt1 = cnt1 + 1
            source_file = os.path.join(root, file)
            destination_file = os.path.join(b_path, file)
            shutil.copy2(source_file, destination_file)
    print("转移完成")
    with open("cnt", "a") as f:
        f.write("\n")
        f.write(str(index+cnt1))
