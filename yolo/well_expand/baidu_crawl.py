import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开百度图片搜索页面
driver.get("https://www.google.com/search?q=%E7%A0%B4%E6%8D%9F%E4%BA%95%E7%9B%96&tbm=isch&hl=zh-CN&chips=q:%E7%A0%B4%E6%8D%9F+%E4%BA%95%E7%9B%96,online_chips:%E4%BA%95%E7%9B%96%E8%A1%A8%E9%9D%A2:ARN8kzQHX1M%3D,online_chips:%E5%A4%8D%E5%90%88%E4%BA%95%E7%9B%96:FgD2yYFAxmI%3D,online_chips:%E5%AE%89%E5%85%A8%E9%9A%90%E6%82%A3:m0R-FjoRuI8%3D&sa=X&ved=2ahUKEwii8Pz6gsuEAxWklmMGHRd7CS0Q4lYoAXoECAEQOg&biw=1519&bih=686")

# 设置滚动次数计数器
scroll_count = 0
max_scroll_count = 5
image_elements_all=[]
# 模拟滚动页面，不断加载更多图片
last_height = driver.execute_script("return document.body.scrollHeight")
while scroll_count < max_scroll_count:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    image_elements = driver.find_elements(By.XPATH, '//*[@id="imgid"]/div[1]/ul/li/div[1]/div[2]/a/img')
    image_elements_all.extend(image_elements)
    new_height = driver.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #     break
    #last_height = new_height
    scroll_count += 1

# 找到所有可见图片元素
print(len(image_elements_all))
# 创建保存图片的文件夹
if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')

# 下载并保存图片
for i, image_element in enumerate(image_elements_all, 1):
    # 获取图片链接
    image_link = image_element.get_attribute("src")
    print(image_link)
    if image_link and image_link.startswith("http"):
        # 发送请求获取图片内容
        response = requests.get(image_link)
        if response.status_code == 200:
            # 保存图片到本地
            with open(f"downloaded_images/image_{i+25}.jpg", 'wb') as f:
                f.write(response.content)
            print(f"图片{i+25}已保存到本地")

# 关闭浏览器
driver.quit()

print("所有图片已保存到 downloaded_images 文件夹中。")
