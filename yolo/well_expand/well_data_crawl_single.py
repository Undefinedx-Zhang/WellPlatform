import requests
import os
from PIL import Image
from io import BytesIO
import mimetypes
import urllib.parse

# 定义图片链接
img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp3A4qsLcuK3oggV-Yuushfq0IFmFK4PgXVg&usqp=CAU"

# 发送请求获取图片
response = requests.get(img_url)

# 检查响应的内容类型是否为图片
content_type = response.headers['Content-Type']
if 'image' not in content_type:
    print("下载的内容不是图片")
    exit()

# 将图片内容读取为 PIL Image 对象
img = Image.open(BytesIO(response.content))

# 获取图片扩展名
content_type_parts = content_type.split('/')
file_extension = mimetypes.guess_extension(content_type_parts[1])

# 确保目录存在
if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')

# 提取图片名称
img_name = os.path.basename(img_url)

# 如果无法确定文件扩展名，则使用默认的 .jpg 扩展名
if file_extension is None:
    img_name_with_extension = img_name + '.jpg'
else:
    img_name_with_extension = img_name + file_extension

# 将文件名中的非法字符替换为下划线
valid_img_name = ''.join(c if c.isalnum() or c in ['.', '_', '-'] else '_' for c in img_name_with_extension)

# 拼接保存路径
save_path = os.path.join('downloaded_images', valid_img_name)

# 保存图片
img.save(save_path)

print(f"图片已保存到：{save_path}")
