# -*- coding:utf-8 -*-

import logging
import os
import requests
import time
from src.db.dbhelper import DBHelper
from src.config import Log
from src.config import config


class Download(object):
    __IMG_PATH = 'imgs' if config.get('env') == 'prd' else 'imgs_test'
    DIR_PATH = os.path.join(os.getcwd(), __IMG_PATH)

    @classmethod
    def downImgs(cls, item):
        """
                下载图片
        :param item:
        :return:
        """
        img_front_status, img_side_status, img_obverse_status = '0', '0', '0'
        has_front, has_side, has_obverse = False, False, False

        item_old = DBHelper.select_item(key='good_id', value=item.good_id)
        if item_old:
            Log.info('在数据库中查到商品信息:good_name: %s, good_upc:%s, status: %s'
                     % (item_old.good_name, item_old.good_upc, item.status))

            if item_old.status.startswith('1'):         # 1xx 表示有正面图片
                img_front_status = '1'
                has_front = True
                item.img_front_local = item_old.img_front_local
                Log.info('已有正面图片: %s' % item_old.img_front_local)
            elif item_old.status[1] == '1':             # x1x 表示有侧面图片
                img_side_status = '1'
                has_side = True
                item.img_side_local = item_old.img_side_local
                Log.info('已有侧面图片: %s' % item_old.img_side_local)
            elif item_old.status.endswith('1'):         # xx1 表示有反面图片
                img_obverse_status = '1'
                has_obverse = True
                item.img_obverse_local = item_old.img_obverse_local
                Log.info('已有反面图片: %s' % item_old.img_obverse_local)
                pass

        else:
            Log.info('没有查到对应商品:%s' % item.good_upc)

        # 正面
        if item.img_front and not has_front:
            Log.info('开始下载图片：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))
            rs = cls.downloadImg(item.img_front, '%s_100' % item.good_upc)
            if rs:
                item.img_front_local = rs
                img_front_status = '1'
                Log.info('图片下载成功：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))
            else:
                Log.info('图片下载失败：upc:%s, 图片类型：正面， 链接：%s' % (item.good_upc, item.img_front))

        # 侧面
        if item.img_side and not has_side:
            Log.info('开始下载图片：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))
            rs = cls.downloadImg(item.img_side, '%s_010' % item.good_upc)
            if rs:
                item.img_side_local = rs
                img_side_status = '1'
                Log.info('图片下载成功：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))
            else:
                Log.info('图片下载失败：upc:%s, 图片类型：侧面， 链接：%s' % (item.good_upc, item.img_side))

        # 反面
        if item.img_obverse and not has_obverse:
            Log.info('开始下载图片：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))
            rs = cls.downloadImg(item.img_obverse, '%s_001' % item.good_upc)
            if rs:
                item.img_obverse_local = rs
                img_obverse_status = '1'
                Log.info('图片下载成功：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))
            else:
                Log.info('图片下载失败：upc:%s, 图片类型：反面， 链接：%s' % (item.good_upc, item.img_obverse))

        item.status = img_front_status + img_side_status + img_obverse_status
        Log.info('待保存的商品信息：%s' % item)
        DBHelper.insert_or_update(item)

    @classmethod
    def downloadImg(cls, img_url, img_name) -> str:
        filename = os.path.join(cls.DIR_PATH, img_name)
        try:
            res = requests.get(img_url, timeout=15)
            if str(res.status_code)[0] == '4':
                return None
        except:
            return None

        f = open(filename + '.jpg', 'wb')
        f.write(res.content)
        f.close()
        return img_name + '.jpg'

    pass


def main():
    pass


if __name__ == '__main__':
    main()
