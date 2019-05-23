# -*- coding:utf-8 -*-
import matplotlib.pyplot as plot
import cv2
import numpy


def open_bmp():
    nm = cv2.imread('pay.bmp')
    print(nm.shape)
    nm_r = nm[:, :, 0]
    print(nm_r.shape)
    cv2.imwrite('test2.bmp', nm_r)
    pass


def rgb_2_grey(r, g, b):
    return int(r * 0.30 + g * 0.59 + b * 0.11)


def open_bmp_file(img_name):
    f_read = open(img_name, 'rb+')
    f_write = open('bmp_data.txt', 'a+')
    data = f_read.read()
    for i in range(len(data)):
        if i % 20 == 0:
            print(data[i])
            f_write.write('\n')
            f_write.write(str(int(data[i])))
        else:
            print(data[i], end='\t')
            f_write.write('\t')
            f_write.write(str(int(data[i])))

    print()
    f_read.close()
    f_write.close()


def read_bmp_header():
    f_read = open('01.bmp', 'rb')
    data = f_read.read()
    f_read.close()
    print('文件总长度：%d' % len(data))
    print('=' * 70)
    data_file_header = data[0:14:]
    print('文件头长度：%d' % len(data_file_header))
    for d in data_file_header:
        print(d, end='\t')

    print()
    print('-' * 70)

    print('文件类型:%d\t%d' % (data_file_header[0], data_file_header[1]))
    print('文件大小：%d\t%d\t%d\t%d' % (data_file_header[5], data_file_header[4], data_file_header[3], data_file_header[2]))
    print('保留字段1：%d\t%d' % (data_file_header[6], data_file_header[7]))
    print('保留字段2：%d\t%d' % (data_file_header[8], data_file_header[9]))
    print('数据偏移：%d\t%d\t%d\t%d' %(data_file_header[13], data_file_header[12], data_file_header[11], data_file_header[10]))

    print('=' * 70)

    data_img_header = [hex(i) for i in data[14:54:]]
    data_img_header_i = [i for i in data[14:54:]]
    print("位图信息头长度：%d" % len(data_img_header))
    for d in data_img_header_i:
        print(d, end='\t')

    print()
    print('-' * 70)

    print('位图信息头所需长度：%s\t%s\t%s\t%s' % (data_img_header[3], data_img_header[2], data_img_header[1], data_img_header[0]))
    print('位图宽度：%s\t%s\t%s\t%s' % (data_img_header[7], data_img_header[6], data_img_header[5], data_img_header[4]))
    print('位图高度：%s\t%s\t%s\t%s' % (data_img_header[11], data_img_header[10], data_img_header[9], data_img_header[8]))
    print('颜色平面数：%s\t%s' % (data_img_header[13], data_img_header[12]))
    print('biBitCount：%s\t%s' % (data_img_header[15], data_img_header[14]))
    print('图像数据的压缩类型：%s\t%s\t%s\t%s' % (data_img_header[19], data_img_header[18], data_img_header[17], data_img_header[16]))
    print('图像大小：%s\t%s\t%s\t%s' % (data_img_header[23], data_img_header[22], data_img_header[21], data_img_header[20]))
    print('水平分辨率（像素/米）：%s\t%s\t%s\t%s' % (data_img_header[27], data_img_header[26], data_img_header[25], data_img_header[24]))
    print('垂直分辨率（像素/米）：%s\t%s\t%s\t%s' % (data_img_header[31], data_img_header[30], data_img_header[29], data_img_header[28]))
    print('实际使用的彩色表中的颜色索引数：%s\t%s\t%s\t%s' % (data_img_header[35], data_img_header[34], data_img_header[33], data_img_header[32]))
    print('对图像显示有重要影响的颜色索引数：%s\t%s\t%s\t%s' % (data_img_header[39], data_img_header[38], data_img_header[37], data_img_header[36]))

    print('='*70)

    data_color_header = data[54:62:]
    print("颜色表长度：%d" % len(data_color_header))
    for d in data_color_header:
        print(d, end='\t')

    data_data = data[62::]
    print('数据长度：%d' % len(data_data))

    pass


def read_bmp_header2():
    f_read = open('01.bmp', 'rb')
    data = f_read.read()
    f_read.close()
    print('文件总长度：%d' % len(data))
    print('=' * 70)
    data_file_header = data[0:14:]
    print('文件头长度：%d' % len(data_file_header))
    for d in data_file_header:
        print(d, end='\t')

    print()
    print('-' * 70)

    print('文件类型:%d\t%d' % (data_file_header[0], data_file_header[1]))
    print('文件大小：%d\t%d\t%d\t%d' % (data_file_header[5], data_file_header[4], data_file_header[3], data_file_header[2]))
    print('保留字段1：%d\t%d' % (data_file_header[6], data_file_header[7]))
    print('保留字段2：%d\t%d' % (data_file_header[8], data_file_header[9]))
    print('数据偏移：%d\t%d\t%d\t%d' %(data_file_header[13], data_file_header[12], data_file_header[11], data_file_header[10]))

    print('=' * 70)

    data_img_header = [hex(i) for i in data[14:54:]]
    data_img_header_i = [i for i in data[14:54:]]
    print("位图信息头长度：%d" % len(data_img_header))
    for d in data_img_header_i:
        print(d, end='\t')

    print()
    print('-' * 70)

    print('位图信息头所需长度：%s\t%s\t%s\t%s' % (data_img_header[3], data_img_header[2], data_img_header[1], data_img_header[0]))
    print('位图宽度：%s\t%s\t%s\t%s' % (data_img_header[7], data_img_header[6], data_img_header[5], data_img_header[4]))
    print('位图高度：%s\t%s\t%s\t%s' % (data_img_header[11], data_img_header[10], data_img_header[9], data_img_header[8]))
    print('颜色平面数：%s\t%s' % (data_img_header[13], data_img_header[12]))
    print('biBitCount：%s\t%s' % (data_img_header[15], data_img_header[14]))
    print('图像数据的压缩类型：%s\t%s\t%s\t%s' % (data_img_header[19], data_img_header[18], data_img_header[17], data_img_header[16]))
    print('图像大小：%s\t%s\t%s\t%s' % (data_img_header[23], data_img_header[22], data_img_header[21], data_img_header[20]))
    print('水平分辨率（像素/米）：%s\t%s\t%s\t%s' % (data_img_header[27], data_img_header[26], data_img_header[25], data_img_header[24]))
    print('垂直分辨率（像素/米）：%s\t%s\t%s\t%s' % (data_img_header[31], data_img_header[30], data_img_header[29], data_img_header[28]))
    print('实际使用的彩色表中的颜色索引数：%s\t%s\t%s\t%s' % (data_img_header[35], data_img_header[34], data_img_header[33], data_img_header[32]))
    print('对图像显示有重要影响的颜色索引数：%s\t%s\t%s\t%s' % (data_img_header[39], data_img_header[38], data_img_header[37], data_img_header[36]))

    print('='*70)

    data_data = data[54::]
    print('数据长度：%d' % len(data_data))
    print('=' * 70)

    data_rows = []

    for i in range(113):
        data_rows.append(data_data[i*1032:i*1032+1032:])
    pass

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

    data_bin.reverse()

    for d in data_bin:
        print(d)

    # 将二值化后的数据转换成字节
    img_data_int = [int('0b' + i[j * 8:j * 8 + 8:], base=0) for i in data_bin for j in range(44)]

    print(len(img_data_int))

def main():
    # open_bmp()
    # open_bmp_file('pay.bmp')
    # open_bmp_file('test2.bmp')
    # read_bmp_header()
    read_bmp_header2()
    pass


if __name__ == '__main__':
    main()
