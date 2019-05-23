# -*- coding:utf-8 -*-
import scrapy
from scrapy import http
from src.scrapy.items import YzgGoodsItem
from src.scrapy import settings
import src.scrapy.tools as tools


class GoodSpider(scrapy.Spider):
    name = "good_hc"

    def __init__(self):
        self.allow_domains = ['baidu.com', 'hc360.com']
        # self.start_urls = [
        #     "https://s.hc360.com/?w=6902018770484&mc=seller&ap=B&pab=B",
        #     # "https://s.hc360.com/?w=6902018770484&mc=seller&ap=B&pab=B",
        # ]
        self.datas = [i for i in tools.get_datas(data_path='data.xls')][1::]
        self.start_urls = ['https://s.hc360.com/?w=%s&mc=seller&ap=B&pab=B' % str(i[4])[6:-1:] for i in self.datas[::]]
        self.__index = 0
        self.__img_has_count = 0  # 爬取到图片的商品数
        self.__img_no_count = 0  # 没有爬取到图片的商品
        print('----goods create over----')

    def parse(self, response):
        print("----start parse: %d----" % self.__index)

        html = response.xpath('/html/body')
        sel = html.xpath(
            './/div[@class="s-layout"]/div[@class="s-mod-main"]/div[@class="cont-left"]/div[@class="wrap-grid"]/ul')

        good_arr = sel.xpath('.//li[@class="grid-list"]/div[@class="NewItem"]')

        if len(good_arr) > 0:
            self.__img_has_count = self.__img_has_count + 1
        else:
            self.__img_no_count = self.__img_no_count + 1

        img_urls = []
        img_deeps = min(len(good_arr), settings.IMAGE_DEEPS)
        for i in range(img_deeps):

            img_data = good_arr[i].xpath('div[@class="picmid pRel"]/a/img')

            if len(img_data) > 0:
                data = str(img_data[0].xpath('@src').extract()[0])
                if data.find('loading.gif') > 0:
                    data = str(img_data[0].xpath('@data-original').extract()[0])

                img_urls.append(data)

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
        item.good_source = 'hc'
        item.write_data()
        print('has_img:%d' % self.__img_has_count)
        print('ni_img:%d' % self.__img_no_count)
        print("----end parse: %d----" % self.__index)
        self.__index = self.__index + 1
        pass


def main():
    help(tools.ImageTool.download)
    pass


if __name__ == '__main__':
    main()
