# -*- coding:utf-8 -*-
import math


def rgb_2_grey(r, g, b):
    return int(r * 0.30 + g * 0.59 + b * 0.11)


def bmp2bmp():
    # 读取文件
    f_read = open('01.bmp', 'rb')
    data = f_read.read()
    f_read.close()

    data_w, data_h, data_old_count, data_new_count = 343, 113, 24, 1
    data_row_old_size = math.ceil(data_w * data_old_count / 32) * 4
    data_row_new_size = math.ceil(data_w * data_new_count / 32) * 4

    # 读取数据，对于数据的分析已经在testbmp.py中解析过
    data_data = data[54::]
    print('数据长度：%d' % len(data_data))

    # 逐行取数
    data_rows = []

    for i in range(data_h):
        data_rows.append(data_data[i * data_row_old_size:i * data_row_old_size + data_row_old_size:])
    pass

    # 二值化
    data_bin = []

    for d in data_rows:
        r = ''
        for k in range(343):
            grey = rgb_2_grey(d[k * 3 + 0], d[k * 3 + 1], d[k * 3 + 2])
            # print(grey, end='\t')
            if grey >= 128:
                r += '1'
            else:
                r += '0'
        r += '000000000'
        data_bin.append(r)

    # data_bin.reverse()

    # 将二值化后的数据转换成字节
    img_data_int = [int('0b' + i[j * 8:j * 8 + 8:], base=0) for i in data_bin for j in range(44)]

    print('文件大小：%d' % (len(img_data_int) + 62))
    print('数据偏移：%d' % 62)
    print('数据大小：%d' % len(img_data_int))

    # 将文件头，信息头，索引表和数据拼接在一起
    data_all = create_file_header() + create_img_header() + create_color_index() + img_data_int

    # 写入文件
    f_write = open('01_new.bmp', 'ab+')
    f_write.write(bytes(data_all))
    f_write.close()


def create_file_header():
    """
    创建文件头
    :return:
    """
    data_file_header = []
    # 0,1 文件类型
    data_file_header.append(66)
    data_file_header.append(77)

    # 2,3,4,5文件大小, 5034
    data_file_header.append(170)
    data_file_header.append(19)
    data_file_header.append(0)
    data_file_header.append(0)

    # 6,7,8,9保留字
    data_file_header.append(0)
    data_file_header.append(0)
    data_file_header.append(0)
    data_file_header.append(0)

    # 数据起始位置偏移
    data_file_header.append(62)
    data_file_header.append(0)
    data_file_header.append(0)
    data_file_header.append(0)
    return data_file_header


def create_img_header():
    """
        创建位图信息头
    :return:
    """
    data_img_header = []

    # 0,1,2,3信息头长度
    data_img_header.append(40)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    # 4,5,6,7图片宽度 343   0x0157  87 1
    data_img_header.append(87)
    data_img_header.append(1)
    data_img_header.append(0)
    data_img_header.append(0)

    # 8,9,10,11图片高度 113 0x71 113
    data_img_header.append(113)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    # 12,13 颜色平面数， 固定为01
    data_img_header.append(1)
    data_img_header.append(0)

    # 14,15 biBitCount 固定为01
    data_img_header.append(1)
    data_img_header.append(0)

    # 16,17,18,19 图像压缩类型， 固定为0000
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    # 20,21,22,23 图像大小，既图像数据的字节数 4972  0x136c  0x6c 0x13  108 19
    data_img_header.append(108)
    data_img_header.append(19)
    data_img_header.append(0)
    data_img_header.append(0)

    # 24,25,26,27 水平分辨率
    data_img_header.append(196)
    data_img_header.append(14)
    data_img_header.append(0)
    data_img_header.append(0)

    # 28,29,30,31 垂直分辨率
    data_img_header.append(196)
    data_img_header.append(14)
    data_img_header.append(0)
    data_img_header.append(0)

    # 32,33,34,35 使用颜色索引数
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    # 36,37,38,39 对显示有重要影响的颜色索引数
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    return data_img_header


def create_color_index():
    """
    创建颜色索引表
    :return:
    """
    data_color_index = [0, 0, 0, 0, 255, 255, 255, 0]
    return data_color_index

def main():
    bmp2bmp()
    pass


if __name__ == '__main__':
    main()