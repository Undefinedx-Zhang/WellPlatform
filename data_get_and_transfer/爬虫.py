# -*- coding: utf-8 -*-
import re
import requests

import os

file = ''
List = []

#爬取图片链接
def Find(url, A):
    global List
    print('正在检测图片总数，请稍等.....')
    s = 0
    try:
        Result = A.get(url, timeout=7, allow_redirects=False)
    except BaseException:
        print("error");
    else:
        result = Result.text
        pic_url = re.findall('<img[^>]*src="(.*?)"[^>]*alt="井盖图片 的图像结果"[^>]*>', result)  # 先利用正则表达式找到图片url
        s += len(pic_url)
        if len(pic_url) == 0:
            print("没读到")
        else:
            List.append(pic_url)
    return s

#下载图片
def dowmloadPicture():
    with open("cnt", "r") as f:
        lines = f.readlines()  # 读取文件的所有行，返回一个包含每行内容的列表
        last_line = lines[-1].strip()  # 获取最后一行内容，并去除首尾空白字符（如换行符等）
        try:
            num = int(last_line)  # 尝试将最后一行内容转换为整数
        except ValueError:
            print("最后一行内容无法转换为整数")
    num=num+1
    for each in List[0]:
        print('正在下载第' + str(num) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            if len(pic.content) < 200:
                continue
            string = file + r'\\'  + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num+=1


if __name__ == '__main__':  # 主函数入口
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Upgrade-Insecure-Requests': '1'
    }

    A = requests.Session()
    A.headers = headers

    url = 'https://cn.bing.com/images/search?q=%E4%BA%95%E7%9B%96%E5%9B%BE%E7%89%87&form=IQFRML&first=1'

    total = Find(url, A)
    print('经过检测图片共有%d张' % (total))
    # file = input('请建立一个存储图片的文件夹，输入文件夹名称即可: ')
    # y = os.path.exists(file)
    # if y == 1:
    #     print('该文件已存在，请重新输入')
    #     file = input('请建立一个存储图片的文件夹，)输入文件夹名称即可: ')
    #     os.mkdir(file)
    # else:
    #     os.mkdir(file)
    file = "./img1"
    dowmloadPicture()
    print('当前爬取结束，感谢使用')

