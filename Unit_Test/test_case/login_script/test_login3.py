# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Login_UZG
import os

filepath = os.getcwd() + ("\\data\\loginTest.xlsx")
sheetName4 = ("Sheet4")
sheetName5 = ("Sheet5")
sheetName6 = ("Sheet6")

datadict4 = ReadExcel.ExcelUtil(filepath, sheetName4).dict_data()
datadict5 = ReadExcel.ExcelUtil(filepath, sheetName5).dict_data()
datadict6 = ReadExcel.ExcelUtil(filepath, sheetName6).dict_data()


@ddt.ddt
class LoginTest(unittest.TestCase):
    '''短信登录测试'''
    a = Login_UZG.OpenUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        self.a.text_login()

    def tearDown(self):
        pass

    @ddt.data(*datadict4)
    def test_login04(self, dat4):
        '''短信登陆—手机号码输入测试—点击登录按钮提示'''
        print dat4
        self.a.login4(dat4['mobilenum'], dat4['validatecode'], dat4[u'result'])

    @ddt.data(*datadict5)
    def test_login05(self, dat5):
        '''短信登陆—验证码输入测试—点击登录按钮提示'''
        print dat5
        self.a.login5(dat5['mobilenum'], dat5['validatecode'], dat5[u'result'])

    @ddt.data(*datadict6)
    def test_login06(self, dat6):
        '''短信登录—手机号码输入测试—点击获取验证码提示'''
        print dat6
        self.a.login6(dat6['mobilenum'], dat6[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)