# -*- coding:utf-8 -*-


class HtmlTool(object):
    """
        html 文件生成工具
    """

    ITEM_COUNT = 2000

    def __init__(self, file_kind):
        self.kind = file_kind
        self.file = None
        self.seq = 0
        pass

    def write_item(self, item):
        """
            写入一个item
        :param item:
        :return:
        """

        if int(int(item.good_id) / HtmlTool.ITEM_COUNT) == self.seq:
            pass
        else:
            self.__create_html('goods_%d_%d.html' % (self.seq*2000, self.seq*2000 + 1999))
            pass

        # 1. 判断self.file
        if self.file:
            pass
        else:
            pass


    def __create_html(self, file_name):

        pass


def f1():
    file_w = open("../../bd_data.txt")
    pass


def main():
    f1()
    pass


if __name__ == '__main__':
    main()