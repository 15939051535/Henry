# -*- coding:utf-8 -*-
import sqlite3
import threading
import time
from src.config import Log
from src.config import config

TABLE_NAME = 'items' if config.get('env') == 'prd' else 'items_test'

CREATE_SQL = '''
            CREATE TABLE IF NOT EXISTS %s(
                good_id INT(10) PRIMARY KEY NOT NULL, 
                good_name VARCHAR(50),
                good_upc VARCHAR(20) NOT NULL,
                good_first VARCHAR(20),
                good_second VARCHAR(20),
                good_third VARCHAR(20),
                good_desc VARCHAR(50),
                good_price VARCHAR(20),
                good_p VARCHAR(20),
                good_c VARCHAR(20),
                good_x VARCHAR(20),
                img_front VARCHAR(200),
                img_side VARCHAR(200),
                img_obverse VARCHAR(200),
                create_time VARCHAR(20),
                status VARCHAR(3),
                img_front_local VARCHAR(100),
                img_side_local VARCHAR(100),
                img_obverse_local VARCHAR(100),
                good_imgs VARCHAR(2000)
            )
''' % TABLE_NAME


class GoodItem(object):
    """
        商品类
    """

    def __init__(self, info_dict={}, info_tuple=()):
        if info_dict:
            self.good_id = info_dict.get('good_id')
            self.good_name = info_dict.get('good_name')
            self.good_upc = info_dict.get('good_upc')
            self.good_first = info_dict.get('good_first')
            self.good_second = info_dict.get('good_second')
            self.good_third = info_dict.get('good_third')
            self.good_desc = info_dict.get('good_desc')
            self.good_price = info_dict.get('good_price')
            self.good_p = info_dict.get('good_p')
            self.good_c = info_dict.get('good_c')
            self.good_x = info_dict.get('good_x')
            self.img_front = info_dict.get('img_front')
            self.img_side = info_dict.get('img_side')
            self.img_obverse = info_dict.get('img_obverse')
            self.status = info_dict.get('img_obverse_local')
            self.img_front_local = info_dict.get('img_front_local')
            self.img_side_local = info_dict.get('img_side_local')
            self.img_obverse_local = info_dict.get('img_obverse_local')
            self.good_imgs = info_dict.get('good_imgs')
            if self.status is None:
                self.status = '000'
        elif info_tuple and len(info_tuple) >= 20:
            self.good_id = info_tuple[0]
            self.good_name = info_tuple[1]
            self.good_upc = info_tuple[2]
            self.good_first = info_tuple[3]
            self.good_second = info_tuple[4]
            self.good_third = info_tuple[5]
            self.good_desc = info_tuple[6]
            self.good_price = info_tuple[7]
            self.good_p = info_tuple[8]
            self.good_c = info_tuple[9]
            self.good_x = info_tuple[10]
            self.img_front = info_tuple[11]
            self.img_side = info_tuple[12]
            self.img_obverse = info_tuple[13]
            self.create_time = info_tuple[14]
            self.status = info_tuple[15]
            self.img_front_local = info_tuple[16]
            self.img_side_local = info_tuple[17]
            self.img_obverse_local = info_tuple[18]
            self.good_imgs = eval(info_tuple[19])


class DBHelper(object):
    """
        数据库连接工具
    """
    conn = sqlite3.connect('data.db', check_same_thread=False)
    cursor = conn.cursor()
    lock = threading.Lock()

    @classmethod
    def init(cls):
        cls.create_table()

        pass

    @classmethod
    def create_table(cls):
        cls.cursor.execute(CREATE_SQL)
        Log.info('数据库初始化完成')

    @classmethod
    def insert_or_update(cls, item):
        i = cls.select_item('good_id', item.good_id)
        if i:
            cls.update_item(item)
        else:
            cls.insert_item(item)

    @classmethod
    def select_item(cls, key='', value=''):
        """
            根据某一列查询商品
        :param key:
        :param value:
        :return:
        """
        cls.lock.acquire()  # 加线程锁
        # cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        select_sql = '''
            SELECT * FROM %s where %s = %s
        ''' % (TABLE_NAME, key, value)
        l = [GoodItem(info_tuple=item) for item in cls.cursor.execute(select_sql)]
        # cls.conn.execute("COMMIT")  # 结束事务
        cls.lock.release()  # 释放锁
        if l:
            return l[0]
        return None

    @classmethod
    def select_items(cls, page=1, page_size=20, options=()) -> list:
        """
            分页查询
        :param options: 查询条件
        :param page:    页数
        :param page_size: 每页步长
        :return:

        """
        cls.lock.acquire()  # 加线程锁
        # cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        op = cls.__join_options(options)

        select_sql = '''
            SELECT * FROM %s %s ORDER BY good_id LIMIT %d OFFSET %d * %d
        ''' % (TABLE_NAME, op, page_size, page - 1, page_size)

        Log.info('数据库分页查询sql: \n%s' % select_sql)
        d = [GoodItem(info_tuple=item) for item in cls.cursor.execute(select_sql)]
        # cls.conn.execute("COMMIT")  # 结束事务
        cls.lock.release()  # 释放锁
        return d

    @classmethod
    def select_count(cls, options=()):
        """
            总量查询
        :param options:  查询条件
        :return:
        """
        cls.lock.acquire()  # 加线程锁
        # cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        op = cls.__join_options(options)

        select_sql = '''
            SELECT count(*) FROM %s %s 
        ''' % (TABLE_NAME, op)
        Log.info('数据库查询总量sql: \n%s' % select_sql)
        res = cls.cursor.execute(select_sql)
        # cls.conn.execute("COMMIT")  # 结束事务
        cls.lock.release()  # 释放锁
        for r in res:
            return r[0]

    @classmethod
    def insert_item(cls, item):
        """
            插入一条商品信息
        :param item:
        :return:
        """
        cls.lock.acquire()  # 加线程锁
        cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        insert_sql = '''
            INSERT INTO %s (good_id, good_name, good_upc, good_first, good_second
            , good_third, good_desc, good_price, good_p, good_c, good_x, img_front
            , img_side, img_obverse, img_front_local, img_side_local, img_obverse_local,create_time, status, good_imgs)
             VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'
             , '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        ''' % (TABLE_NAME, item.good_id, item.good_name.replace('\'', '\'\''), item.good_upc, item.good_first,
               item.good_second,
               item.good_third, item.good_desc.replace('\'', '\'\''), item.good_price, item.good_p, item.good_c,
               item.good_x, item.img_front, item.img_side, item.img_obverse, item.img_front_local,
               item.img_side_local, item.img_obverse_local, time_str, item.status,
               str(item.good_imgs).replace('\'', '\'\''))

        Log.info('数据库新增商品sql: \n%s' % insert_sql)
        cls.cursor.execute(insert_sql)
        cls.conn.execute("COMMIT")  # 结束事务
        Log.info('数据库添加商品成功：商品名：%s, upc: %s, 状态：%s' % (item.good_name, item.good_upc, item.status))
        cls.lock.release()  # 释放锁

    @classmethod
    def update_item(cls, item):
        """
            更新一条商品信息
        :param item:
        :return:
        """
        cls.lock.acquire()  # 加线程锁
        cls.conn.execute("BEGIN TRANSACTION")  # 开启事务
        update_sql = '''
            UPDATE %s SET img_front = '%s', img_side = '%s', img_obverse = '%s', status = '%s', img_front_local = '%s', 
            img_side_local = '%s', img_obverse_local = '%s' where good_id = %s
        ''' % (TABLE_NAME, item.img_front, item.img_side, item.img_obverse, item.status, item.img_front_local,
               item.img_side_local, item.img_obverse_local, item.good_id)

        Log.info('数据库更新商品sql: \n%s' % update_sql)

        try:
            cls.cursor.execute(update_sql)
            cls.conn.commit()  # 结束事务
            Log.info('数据库更新商品成功：商品名：%s, upc: %s, 状态：%s' % (item.good_name, item.good_upc, item.status))
        finally:
            cls.lock.release()  # 释放锁

    @classmethod
    def execute_sql(cls, sql):
        pass

    @classmethod
    def __join_options(cls, options) -> str:
        """
            拼接查询条件
        :param options:
        :return:
        """
        op = ''
        if options:
            op += ' where'
            for p in options:
                op += ''' %s and ''' % p
            op += ' 1=1 '
        return op


def main():
    # DBHelper.init()
    # print(DBHelper.select_count())
    param = {}
    item = GoodItem(param)
    print(item.status)


if __name__ == '__main__':
    main()