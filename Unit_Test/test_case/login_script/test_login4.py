# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Login_forgetpwd
import os

filepath = os.getcwd() + "\\data\\loginTest.xlsx"
sheetName7 = "Sheet7"
sheetName8 = "Sheet8"
sheetName9 = "Sheet9"
sheetName10 = "Sheet10"
datadict7 = ReadExcel.ExcelUtil(filepath, sheetName7).dict_data()
datadict8 = ReadExcel.ExcelUtil(filepath, sheetName8).dict_data()
datadict9 = ReadExcel.ExcelUtil(filepath, sheetName9).dict_data()
datadict10 = ReadExcel.ExcelUtil(filepath, sheetName10).dict_data()


@ddt.ddt
class LoginTest(unittest.TestCase):
    """忘记密码—修改密码测试"""
    a = Login_forgetpwd.ForgetPwd()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.forget_pwd()
        cls.a.forget_iframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.forget_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict7)
    def test_login07(self, dat7):
        """修改密码—手机号码输入框测试"""
        print dat7
        self.a.login7(dat7['phonenumber'],  dat7[u'result'])

    @ddt.data(*datadict8)
    def test_login08(self, dat8):
        """修改密码—验证码输入框测试"""
        print dat8
        self.a.login8(dat8['phonenumber'], dat8['messgescode'], dat8[u'result'])

    @ddt.data(*datadict9)
    def test_login09(self, dat9):
        """修改密码—设置新密码输入测试"""
        print dat9
        self.a.login9(dat9['phonenumber'], dat9['messgescode'], dat9['newpassword'], dat9[u'result'])

    @ddt.data(*datadict10)
    def test_login10(self, dat10):
        """修改密码—再次输入新密码输入测试"""
        print dat10
        self.a.login10(dat10['phonenumber'], dat10[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)