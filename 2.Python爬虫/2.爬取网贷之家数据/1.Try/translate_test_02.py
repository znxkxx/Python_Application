# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:22:00 2017

@author: XuXin
"""

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['i'] = '翻译'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = 1514362549969
    Form_Data['sign'] = '6e8b9010ac540da801e67770c8affcd0'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data['typoResult'] = 'false'
    
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
           
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data,headers=headers)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    # translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("The results is: %s" % translate_results)
