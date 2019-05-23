# -*- coding:utf-8 -*-

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

import math
import random
from threading import Thread
from flask import Flask, request, render_template, url_for, send_file, send_from_directory, Response, jsonify

from src.db.dbhelper import GoodItem
from src.db.dbhelper import DBHelper
from src.tools import Download
from src.threadmanager import ThreadManager
from src.config import config
from src.config import Log


IMG_PATH = 'imgs' if config.get('env') == 'prd' else 'imgs_test'

app = Flask(__name__, static_folder=IMG_PATH)
DIR_PATH = os.path.join(os.getcwd(), IMG_PATH)


def response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp


@app.route('/uploadImg', methods=['POST'])
def upload_img():
    """
        上传图片
    :return:
    """
    Log.info('*' * 25 + '接到请求: /uploadImg' + '*' * 25)
    try:
        params = request.form.to_dict()
        Log.info('upload_img:%s' % str(params))
        item = GoodItem(params)
    except:
        return jsonify({'returnCode': '9999', 'returnMessage': '参数异常'})

    # 开启线程下载图片
    # ThreadManager.execute(target=downImgs, args=(item,))
    t = Thread(target=Download.downImgs, args=(item,))
    t.start()
    status_front, status_side, status_obverse = '0', '0', '0'
    if item.img_front:
        status_front = '1'
    if item.img_side:
        status_side = '1'
    if item.img_obverse:
        status_obverse = '1'
    Log.info('*' * 25 + '结束请求' + '*' * 25)
    Log.info('\n')
    return jsonify({'returnCode': '0000', 'returnMessage': '操作成功', 'status': (status_front + status_side + status_obverse)})


@app.route('/', methods=['GET'])
def index():
    """首页"""
    Log.info('*' * 25 + '收到访问请求: /' + '*' * 25)
    count = DBHelper.select_count()
    Log.info('数据总量：%d' % count)
    data = [i + 1 for i in range(math.ceil(count / config.get('page_size')))]
    Log.info('*' * 25 + '/ 请求处理完毕' + '*' * 25)
    return render_template('index.html', data=data)


@app.route('/import', methods=['GET'])
def import_exl():
    return render_template('import.html')
    pass


@app.route('/uploadExl', methods=['POST'])
def upload_exl():
    # 100kb
    # 1.上传操作 耗时1000ms

    # 2. 开启线程，读取上传上来的excel文件，然后将读取后的商品信息列表加入到数据库中 耗时2000ms

    # 2.1 数据保存完成后， 通知爬虫程序开始爬去图片

    # 3. 将处理结果返回给浏览器
    return jsonify({'returnCode': '0000', 'returnMessage': '操作成功'})

    pass


@app.route('/result', methods=['GET'])
def result():
    """结果页"""
    count_front = DBHelper.select_count(options=(''' status like '1__' ''',))
    count_side = DBHelper.select_count(options=(''' status like '_1_' ''',))
    count_obverse = DBHelper.select_count(options=(''' status like '__1' ''',))
    count = DBHelper.select_count()
    data = {'count': count, 'count_front': count_front, 'count_side': count_side, 'count_obverse': count_obverse}
    return render_template('result.html', data=data)


@app.route('/getResultPage', methods=['POST'])
def get_result_page():
    """
        根据不同的查询条件获取结果的页数
    :return:
    """
    Log.info('*' * 25 + '接到请求: /getResultPage' + '*' * 25)
    try:
        params = request.form.to_dict()
        Log.info('getResultPage:%s' % str(params))
        status = params.get('status')
        if status == '000':
            return jsonify({'returnCode': '9999', 'returnMessage': '请至少勾选一项'})

        status = status.replace('0', '_')
        count = DBHelper.select_count(options=(''' status like '%s' ''' % status,))
        pages = math.ceil(count / config.get('page_size'))
        Log.info('*' * 25 + '/getResultPage 请求处理完毕:操作成功' + '*' * 25)
        return jsonify({'returnCode': '0000', 'returnMessage': '操作成功', 'pages': pages})
    except:
        Log.info('*' * 25 + '/getResultPage 请求处理完毕:参数异常' + '*' * 25)
        return jsonify({'returnCode': '9999', 'returnMessage': '参数异常'})


@app.route('/items/<page>', methods=['GET'])
def items(page=None):
    """
        分页查询页
    :param page:
    :return:
    """
    Log.info('*' * 25 + '收到访问请求: /items/%s' % str(page) + '*' * 25)
    if page is None:
        return 'page is None'
    else:
        data = DBHelper.select_items(page=int(page), page_size=config.get('page_size'))
        return render_template('items.html', data=data)


@app.route('/resultList', methods=['GET'])
def result_list():
    """
        查询结果页
    :return:
    """
    Log.info('*' * 25 + '收到访问请求: /resultList' + '*' * 25)
    params = request.args.to_dict()
    Log.info('resultList:%s' % str(params))
    page = params.get('page')
    status = params.get('status').replace('0', '_')
    data = DBHelper.select_items(int(page), config.get('page_size'), options=(''' status like '%s' ''' % status,))
    return render_template('resultList.html', data=data)
    pass


@app.route('/htmls/common.css', methods=['GET'])
def get_common_css():
    return send_from_directory('htmls', 'common.css')


@app.route('/htmls/common.js', methods=['GET'])
def get_common_js():
    return send_from_directory('htmls', 'common.js')


@app.route('/htmls/jquery-3.3.1.js', methods=['GET'])
def get_jquery():
    return send_from_directory('htmls', 'jquery-3.3.1.js')


def main():
    DBHelper.init()
    # 1. 开启web服务器
    # 设置本机ip
    f = open('./htmls/common.js', 'r', encoding='utf-8')
    f.seek(0)
    ls = f.readlines()
    ls[0] = '''const PATH_HOST = 'http://%s:%s' \n''' % (config.get('host'), config.get('port'))
    f.close()

    f = open('./htmls/common.js', 'w', encoding='utf-8')
    for l in ls:
        f.write(l)
    f.close()

    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=config.get('port'))

    Log.info('运行环境：%s' % config.get('env'))

    # l = DBHelper.select_items()
    # print(l[0])
    # 2. 开启爬虫进程, 等带任务通知, 接到通知之后，开始查询数据库，将没有爬去过的商品信息读出来，开始爬去图片,爬去完成后
    # 将结果更新到数据库中,处理完成之后，休眠，等下次的任务通知


    pass


if __name__ == '__main__':
    main()
