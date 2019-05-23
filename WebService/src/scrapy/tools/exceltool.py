# -*- coding:utf-8 -*-
import xlrd
import sys


class ExcelTool(object):



    pass


def f1():
    """
    测试读取
    :return:
    """
    bk = xlrd.open_workbook("data.xls")
    sh = bk.sheet_by_index(0)
    print('rows: %d, cols: %d' % (sh.nrows, sh.ncols))

    data_row = sh.get_rows()
    for data in data_row:

        pass

    # help(sh)

    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
