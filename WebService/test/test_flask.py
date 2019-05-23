# -*- coding:utf-8 -*-

from flask import abort, redirect, url_for, Flask
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/user/')
def index():
    print(url_for('index', id=10, name='XeanYu', age=16))
    return 'Test'


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080, debug=True)

# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
#
# @app.route('/login')
# def login():
#     # abort(401)
#     return "Test"


# if __name__ == '__main__':
#     app.run()