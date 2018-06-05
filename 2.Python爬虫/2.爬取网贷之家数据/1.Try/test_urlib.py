# -*- coding: UTF-8 -*-

# =======================================================
#part 1. 设定python默认编码为utf-8.
# http://blog.csdn.net/jim7424994/article/details/22675759
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
res=urllib.request.urlopen('http://www.baidu.com')
htmlBytes=res.read()
print(htmlBytes.decode('utf-8'))
# =======================================================


# =======================================================
# 抓取一个静态网页，并且格式化输出
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    html = html.decode("utf-8")
    print(html)
# =======================================================




# =======================================================
# 测试 网页的编码格式
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)
# =======================================================
