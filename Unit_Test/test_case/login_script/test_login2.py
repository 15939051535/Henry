# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Login_UZG
import os

# filepath = os.getcwd() + ("\\data\\loginTest.xlsx")
filepath = 'D:\\Unit_Test\\data\\loginTest.xlsx'
sheetName3 = "Sheet3"
datadict3 = ReadExcel.ExcelUtil(filepath, sheetName3).dict_data()


@ddt.ddt
class LoginTest(unittest.TestCase):
    '''店员及掌柜登录测试'''
    a = Login_UZG.OpenUZG()

    def setUp(self):
        self.a.open_uzg()

    def tearDown(self):
        self.a.quit_uzg()

    @ddt.data(*datadict3)
    def test_login03(self, dat3):
        '''店员、店长及掌柜登录测试'''
        print dat3
        self.a.login3(dat3['username'], dat3['password'], dat3[u'result'])

if __name__ == "__main__":
    unittest.main(verbosity=2)