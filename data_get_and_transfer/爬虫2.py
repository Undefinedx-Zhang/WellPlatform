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
        texts = re.findall('<li class="title">\s*<a[^>]*>(.*?)</a>\s*</li>', result)  # 先利用正则表达式找到图片url
        s += len(texts)
        if len(texts) == 0:
            print("没读到")
        else:
            List.append(texts)
    return s
#下载图片
def dowmloadPicture():
    num = 1
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

    url = 'https://movie.douban.com/'
    #
    total = Find(url, A)
    for texts in List:
        for text in texts:
            print(text)

