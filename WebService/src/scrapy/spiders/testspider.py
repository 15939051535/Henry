# -*- coding:utf-8 -*-
import scrapy
from src.scrapy.items import YzgGoodsItem
from src.scrapy.tools.imagetool import ImageTool
from src.scrapy import settings


class TestSpider(scrapy.Spider):

    name = "good_test"

    def __init__(self):
        self.start_urls = [
            "https://s.hc360.com/?w=6901043810042&mc=seller&ap=B&pab=B",
        ]

    def parse(self, response):
        print("----start parse----")
        html = response.xpath('/html/body')
        sel = html.xpath('.//div[@class="s-layout"]/div[@class="s-mod-main"]/div[@class="cont-left"]/div[@class="wrap-grid"]/ul')

        good_arr = sel.xpath('.//li[@class="grid-list"]/div[@class="NewItem"]')

        for li in good_arr:
            if li.xpath('div[@class="picmid pRel"]/a/img/@src').extract():
                print(li.xpath('div[@class="picmid pRel"]/a/img/@src').extract())

        print("----end parse----")
        pass


def main():
    help(ImageTool.download)
    pass


if __name__ == '__main__':
    main()
