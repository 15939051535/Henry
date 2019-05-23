# -*- coding:utf-8 -*-
import scrapy
import re
import urllib
import itertools
from scrapy import http
from src.scrapy.items import YzgGoodsItem
from src.scrapy import settings
import src.scrapy.tools as tools


class GoodSpider(scrapy.Spider):
    name = "good_bd"

    def __init__(self):
        self.allow_domains = ['baidu.com']

        self.re_url = re.compile(r'"objURL":"(.*?)"')

        self.datas = [i for i in tools.get_datas(data_path='data.xls')][1::]
        self.start_urls = [
            'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word=%s&face=0&istype=2nc=1&pn=0&rn=60' % str(
                i[4])[6:-1:] for i in self.datas[::]]
        self.__index = 0
        self.__img_has_count = 0  # 爬取到图片的商品数
        self.__img_no_count = 0  # 没有爬取到图片的商品

        print(self.start_urls)

        print('----goods create over----')



    def parse(self, response):
        print("----start parse: %d----" % self.__index)

        img_urls = self.re_url.findall(str(response.body, encoding='utf-8'))

        if len(img_urls) > settings.IMAGE_DEEPS:
            img_urls = img_urls[0:settings.IMAGE_DEEPS:]

        img_urls = [GoodSpider.decodeImgUrl(x) for x in img_urls]

        item = YzgGoodsItem()
        item.good_p = str(self.datas[self.__index][0])[6:-1:]
        item.good_c = str(self.datas[self.__index][1])[6:-1:]
        item.good_x = str(self.datas[self.__index][2])[6:-1:]
        item.good_upc = str(self.datas[self.__index][3])[6:-1:]
        item.good_name = str(self.datas[self.__index][4])[6:-1:]
        item.good_spec = str(self.datas[self.__index][5])[6:-1:]
        item.good_kind = str(self.datas[self.__index][6])[6:-1:]
        item.good_sub = str(self.datas[self.__index][7])[6:-1:]
        item.good_desc = str(self.datas[self.__index][8])[6:-1:]
        item.good_price = str(self.datas[self.__index][9])[6:-1:]
        item.good_imgs = img_urls
        item.good_id = self.__index
        item.good_source = 'bd'
        item.write_data()



        print('第 %d 条 爬取完成' % self.__index)

        print("----end parse: %d----" % self.__index)
        self.__index = self.__index + 1
        pass

    @classmethod
    def decodeImgUrl(cls, url) -> str:
        for key, value in str_table.items():
            url = url.replace(key, value)
        return url.translate(char_table)






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



def main():
    help(tools.ImageTool.download)
    pass


if __name__ == '__main__':
    main()
