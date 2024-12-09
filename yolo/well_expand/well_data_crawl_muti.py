import base64
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开 Google 图片搜索页面
driver.get(
    "https://www.google.com/search?q=%E7%A0%B4%E6%8D%9F%E4%BA%95%E7%9B%96&sca_esv=cbfd67036d7e3dce&sca_upv=1&bih=686&biw=1519&hl=zh-CN&tbm=isch&sxsrf=ACQVn09eeJ79C1QiyXX8kvCuW0dDc_AYZQ:1709008209057&source=lnms")

# 找到所有图片元素
image_elements = driver.find_elements(By.XPATH, "//img")

# 获取前100张图片链接
image_links = []
for i in range(1000):
    # 检查索引是否超出范围
    if i >= len(image_elements):
        print("已达到页面中的最大图片数量")
        break

    # 获取图片的 base64 编码数据
    base64_data = image_elements[i].get_attribute("src")

    # 检查是否为 None
    if base64_data is None:
        print("图片链接为空")
        continue

    # 检查是否包含逗号
    if "," not in base64_data:
        print("图片数据不包含逗号")
        continue

    try:
        # 将 base64 数据解码为图片
        image_data = base64.b64decode(base64_data.split(",")[1])
        image = Image.open(BytesIO(image_data))

        # 将图像转换为 RGB 模式
        image = image.convert("RGB")
    except Exception as e:
        print(f"无法识别图像文件：{e}")
        continue

    # 确保目录存在
    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    # 保存图片文件
    image_path = f"downloaded_images/image_{i + 1}.jpg"
    image.save(image_path)

    # 添加图片文件路径作为图片链接
    image_links.append(image_path)

# 打印前100张图片链接
for link in image_links:
    print(link)

# 关闭浏览器
driver.quit()
