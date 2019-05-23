# -*- coding:utf-8 -*-
import cv2
import math
import matplotlib.pyplot as plot
import matplotlib.image as im
import numpy


def rgb_2_grey(r, g, b):
    return int(r * 0.30 + g * 0.59 + b * 0.11)


def get_grey(img_arr):
    arr_r, arr_g, arr_b = img_arr[:, :, 0], img_arr[:, :, 1], img_arr[:, :, 2]
    img_width, img_height, img_deep = img_arr.shape
    return [[rgb_2_grey(arr_r[i][j], arr_g[i][j], arr_b[i][j])
             for j in range(img_height)] for i in range(img_width)]


def get_grey_cv2(img_arr):
    arr_r, arr_g, arr_b = img_arr[:, :, 0], img_arr[:, :, 2], img_arr[:, :, 1]
    img_width, img_height, img_deep = img_arr.shape
    return [[rgb_2_grey(arr_r[i][j], arr_g[i][j], arr_b[i][j])
             for j in range(img_height)] for i in range(img_width)]


def ana_nm_2_bmp(nm):
    """

    :param nm:
    :return:
    """
    img_w, img_h, img_d = nm.shape
    # 计算每一行的字节数
    img_row_size = math.ceil(img_w * 1 / 32) * 4

    # 计算补齐后的数据字节大小
    img_data_size = img_row_size * img_h

    # 计算数据区的偏移值
    #   = 文件头字节数（固定14个字节）
    #   + 位图信息头字节数（固定40个字节）
    #   + 颜色索引表字节数（不固定，4的倍数个字节，在位图信息头中可由32-35个字节的值决定（从0开始计）例：00000100 = 256，则索引表字节数 = 256 * 4）

    img_offset_size = 14 + 40 + 8
    # 计算文件总字节数
    img_file_size = img_data_size + img_offset_size
    return img_w, img_h, img_d, img_row_size, img_data_size, img_offset_size, img_file_size


def png_2_bmp(path):
    nm = cv2.imread(path)

    print(nm.shape)
    img_w, img_h, img_d, img_row_size, img_data_size, img_offset_size, img_file_size = ana_nm_2_bmp(nm)

    print('每一行的字节数：%d' % img_row_size)
    print('数据区字节数：%d' % img_data_size)
    print('文件总字节数：%d' % img_file_size)

    # 将图片灰度化
    if img_d >= 3:
        img_grey = get_grey_cv2(nm)
    else:
        return

    # 将图像二值化
    img_data_str = []
    for i in range(img_h):
        r = ''
        for j in range(img_row_size * 8):

            if j < img_w:
                if img_grey[i][j] > 128:
                    r += '1'
                else:
                    r += '0'
            else:
                r += '0'

        img_data_str.append(r)

    # print(img_data_str)
    img_data_str.reverse()

    # 将二值化后的数据转换成字节
    img_data_int = [int('0b' + i[j * 8:j * 8 + 8:], base=0) for i in img_data_str for j in range(img_row_size)]


    # 将文件头，信息头，索引表和数据拼接在一起
    data_all = create_file_header() + create_img_header() + create_color_index() + img_data_int

    # 写入文件
    f_write = open('logo.bmp', 'ab+')
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

    # 2,3,4,5文件大小
    data_file_header.append(194)
    data_file_header.append(3)
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

    # 4,5,6,7图片宽度
    data_img_header.append(75)
    data_img_header.append(0)
    data_img_header.append(0)
    data_img_header.append(0)

    # 8,9,10,11图片高度
    data_img_header.append(75)
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

    # 20,21,22,23 图像大小，既图像数据的字节数
    data_img_header.append(132)
    data_img_header.append(3)
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


def test_bin():
    s = '111100000000000000000000000000000000000000000000000000000000000000000001111000000000000000000000'
    s_list = ['0b' + s[i * 8:i * 8 + 8:] for i in range(12)]

    print(s)
    print(s_list)
    print(s_list[0])
    # help(int)
    print(int(s_list[0], base=0))
    pass


def main():
    png_2_bmp('logo.png')
    # test_bin()
    pass


if __name__ == '__main__':
    main()
