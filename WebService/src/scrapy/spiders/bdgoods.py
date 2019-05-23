# -*- coding:utf-8 -*-
import requests
import os
import re
# import json
import itertools
import urllib
import sys
import src.scrapy.tools as tools
from src.scrapy.items import YzgGoodsItem
from scrapy import settings
from urllib.parse import quote


# 百度图片URL解码
# http://blog.csdn.net/hbuxiaoshe/article/details/44780653
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}
char_table = {ord(key): ord(value) for key, value in char_table.items()}


# 解码
def decode(url):
    for key, value in str_table.items():
        url = url.replace(key, value)
    return url.translate(char_table)


# 百度图片下拉
def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    return urls


re_url = re.compile(r'"objURL":"(.*?)"')


# 获取imgURL
def resolveImgUrl(html):
    imgUrls = [decode(x) for x in re_url.findall(html)]
    img_Urls = [x for x in re_url.findall(html)]
    print('*' * 50)
    print(img_Urls)
    print('*' * 50)
    return imgUrls


# 下载图片
def downImgs(imgUrl, dirpath, imgName, imgType):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=15)
        if str(res.status_code)[0] == '4':
            print(str(res.status_code), ":", imgUrl)
            return False
    except Exception as e:
        print('抛出异常:', imgUrl)
        print(e)
        return False
    with open(filename + '.' + imgType, 'wb') as f:
        f.write(res.content)
    return True


# 创建文件路径
def mkDir(dirName):
    dirpath = os.path.join(sys.path[0], dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


def main():
    img_datas = [i for i in tools.get_datas(data_path='data.xls')][1:2:]
    start_urls = [
        'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word=%s&face=0&istype=2nc=1&pn=0&rn=60'
        % str(i[4])[6:-1:] for i in img_datas[::]
    ]

    for i in range(len(start_urls)):
        print('正在请求：%s ' % start_urls[i])
        print('正在搜索的商品：%s' % str(img_datas[i][4])[6:-1:])
        html = requests.get(start_urls[i], timeout=10).content.decode('utf-8')
        img_urls = resolveImgUrl(html)

        print(img_urls)
        if len(img_urls) == 0:  # 没有图片则结束
            break

        if len(img_urls) > settings.IMAGE_DEEPS:
            img_urls = img_urls[0:settings.IMAGE_DEEPS:]

        item = YzgGoodsItem()
        item.good_p = str(img_datas[i][0])[6:-1:]
        item.good_c = str(img_datas[i][1])[6:-1:]
        item.good_x = str(img_datas[i][2])[6:-1:]
        item.good_upc = str(img_datas[i][3])[6:-1:]
        item.good_name = str(img_datas[i][4])[6:-1:]
        item.good_spec = str(img_datas[i][5])[6:-1:]
        item.good_kind = str(img_datas[i][6])[6:-1:]
        item.good_sub = str(img_datas[i][7])[6:-1:]
        item.good_desc = str(img_datas[i][8])[6:-1:]
        item.good_price = str(img_datas[i][9])[6:-1:]
        item.good_imgs = img_urls
        item.good_id = str(i)
        item.good_source = 'bd'
        item.write_data()

    pass


if __name__ == '__main__':

    main()
