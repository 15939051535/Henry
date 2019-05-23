# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Checkstand_package1

filepath = ("D:\\Unit_Test\\data\\checkstandTest.xlsx")

sheetName1 = ("Sheet1")
sheetName2 = ("Sheet2")
sheetName3 = ("Sheet3")

datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data()
datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data()
datadict3 = ReadExcel.ExcelUtil(filepath, sheetName3).dict_data()

@ddt.ddt
class LoginTest (unittest.TestCase):

    a = Checkstand_package1.shyt()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.click_shyt()
        cls.a.input_shytiframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
       self.a.click_lastCountUl()

    @ddt.data(*datadict1)
    def test_login(self, dat1):
        """收银台会员结算"""
        print dat1
        self.a.login1(dat1['vip'], dat1['barCode'], dat1[u'str1'], dat1[u'str2'], dat1[u'str3'], dat1[u'str4'])

    @ddt.data(*datadict2)
    def test_login1(self, dat2):
        """不打印小票结算"""
        print dat2
        self.a.login2(dat2['vip'], dat2['barCode'], dat2[u'str1'], dat2[u'str2'], dat2[u'str3'], dat2[u'str4'])

    @ddt.data(*datadict3)
    def test_login3(self, dat3):
        """挂单取单销售"""
        print dat3
        self.a.login3(dat3['vip'], dat3['barCode'], dat3[u'str1'], dat3[u'str2'], dat3[u'str3'], dat3[u'str4'])

if __name__ == "__main__":
    unittest.main(verbosity=2)