# -*- coding:utf-8 -*-
import threadpool


class ThreadManager(object):
    """
        线程管理类
    """

    pool = threadpool.ThreadPool(10)

    @classmethod
    def init(cls):
        """
            初始化线程管理器
        :return:
        """
        pass

    @classmethod
    def execute(cls, target, args=()):
        """
            添加一个任务
        :param args:
        :param target:
        :return:
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
