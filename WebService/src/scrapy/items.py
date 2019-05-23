# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# CREATE TABLE yzg_goods(
#   id VARCHAR(10) NOT NULL,
#   prov VARCHAR(20),
#   city VARCHAR(20),
#   town VARCHAR(20),
#   upc VARCHAR(20),
#   name VARCHAR(100),
#   kind_first VARCHAR(20),
#   kind_second VARCHAR(20),
#   kind_third VARCHAR(20),
#   desc VARCHAR(100),
#   price VARCHAR(10),
#   imgs: VARCHART(2000)
#   );



import scrapy
import os
import requests
import json
from src.scrapy.tools.imagetool import ImageTool


class YzgGoodsItem():
    # define the fields for your item here like:
    # name = scrapy.Field()
    # good_id = scrapy.Field()        # 商品序号
    # good_upc = scrapy.Field()       # 商品条码
    # good_name = scrapy.Field()      # 商品名称
    # good_spec = scrapy.Field()      # 商品规格
    # good_imgs = scrapy.Field()      # 商品图片列表

    def __init__(self):
        self.good_source = ''  # 商品来源
        self.good_id = ''  # 商品序号
        self.good_p = ''  # 商品省邮政机构
        self.good_c = ''  # 商品市邮政机构
        self.good_x = ''  # 商品区县邮政机构
        self.good_upc = ''  # 商品条码
        self.good_name = ''  # 商品名称
        self.good_first = ''  # 商品一级分类
        self.good_second = ''  # 商品二级分类
        self.good_third = ''  # 商品三级分类
        self.good_desc = ''  # 商品简述
        self.good_price = ''  # 商品价格
        self.good_imgs = []  # 商品图片列表

    # 下载图片
    def downImgs(self, imgUrl, dirPath, imgName, imgType):
        filename = os.path.join(dirPath, imgName)
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

    def write_data(self):

        file = open('bd_data_2.txt', 'a+', encoding='utf-8')

        # # 省机构，市机构，区县机构，条码，名称，规格，类型，子类，描述，价格
        # file.write('[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d]'
        #                  % (str(self.good_id), self.good_p, self.good_c, self.good_c,
        #                     str(self.good_upc), str(self.good_name), str(self.good_spec),
        #                     str(self.good_kind), str(self.good_sub), str(self.good_desc),
        #                     str(self.good_price), self.good_imgs, len(self.good_imgs)))

        d = {}
        d['good_id'] = self.good_id
        d['good_p'] = self.good_p
        d['good_c'] = self.good_c
        d['good_x'] = self.good_x
        d['good_upc'] = self.good_upc
        d['good_name'] = self.good_name
        d['good_first'] = self.good_first
        d['good_second'] = self.good_second
        d['good_third'] = self.good_third
        d['good_desc'] = self.good_desc
        d['good_price'] = self.good_price
        d['good_imgs'] = self.good_imgs

        file.write(str(d))

        file.write('\n')
        file.close()

        pass


def main():
    file = open('data.txt', 'a+')
    file.write('//img001.hc360.cn/k1/M05/53/76/wKhQwFehlyOEJXjnAAAAADKz4tI853.jpg..220x220a.jpg')
    file.close()
    pass


if __name__ == '__main__':
    main()
