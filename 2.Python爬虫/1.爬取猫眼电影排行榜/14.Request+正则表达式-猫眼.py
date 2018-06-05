# -*- coding: UTF-8 -*-
# 流程框架：

'''
目标：
-----
爬取得猫眼电影榜单，地址：http://maoyan.com/board/4


流程框架
-------
1. 抓取单页内容，利用request请求目标站点，得到单个网页的html代码，范围结果
2. 正则表达式分析，根据html代码分析得到电影的名称、主演、上映时间、评分、图片等链接
3. 保存至文件，通过文件的形式把结果保存，每一个电影一个结果一行Json字符串
4. 开启多线程循环，针对多页内容便利，开启多线程提高抓取速度
'''
import requests
from requests.exceptions import RequestException
import re 


def get_one_page(url):
    # This function used to return one single page
    # 添加错误判断
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None



def parse_one_page(html):
    # 用于拆分单独网页，提取信息
    pattern =     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)  # 返回结果是一个类
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:], # strip()函数用于去除空白字符，再用切片提取有效信息
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }
    

def main():
    url = "http://maoyan.com/board/4?"
    html = get_one_page(url)
    parse_one_page(html)
    # for item in parse_one_page(html):
    #     print(item)


if __name__ == '__main__':
    main()
