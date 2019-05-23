# -*- coding:utf-8 -*-
import xlrd

__all__ = ['url_format']

from src.scrapy.tools.imagetool import ImageTool
from src.scrapy.tools.htmltool import HtmlTool


# url格式化
def url_format(url_pre) -> str:
    """
    将给定的字符串格式化成url
    :param url_pre:
    :return:
    """
    if url_pre.startswith('//'):
        return 'http:' + url_pre
    elif url_pre.startswith('www'):
        return 'http://' + url_pre
    elif url_pre.startswith('http://') or url_pre.startswith('https://'):
        return url_pre
    else:
        return 'http://' + url_pre
    pass


def get_datas(data_path) -> list:
    return xlrd.open_workbook(data_path).sheet_by_index(0).get_rows()


def main():
    pass


if __name__ == '__main__':
    main()