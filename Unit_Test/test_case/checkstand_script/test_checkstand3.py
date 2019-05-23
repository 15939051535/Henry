# coding=utf-8

import unittest
import ddt
import time
from test_common import ReadExcel
from test_common import Checkstand_package2

filepath = ("D:\\Unit_Test\\data\\checkstandTest.xlsx")
sheetName9 = ("Sheet9")
sheetName10 = ("Sheet10")
sheetName11 = ("Sheet11")
sheetName12 = ("Sheet12")
sheetName13 = ("Sheet13")
datadict9 = ReadExcel.ExcelUtil(filepath, sheetName9).dict_data()
datadict10 = ReadExcel.ExcelUtil(filepath, sheetName10).dict_data()
datadict11 = ReadExcel.ExcelUtil(filepath, sheetName11).dict_data()
datadict12 = ReadExcel.ExcelUtil(filepath, sheetName12).dict_data()
datadict13 = ReadExcel.ExcelUtil(filepath, sheetName13).dict_data()


@ddt.ddt
class LoginTest (unittest.TestCase):

    a = Checkstand_package2.right()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        time.sleep(7)
        cls.a.click_shyt()
        cls.a.input_shytiframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @ddt.data(*datadict9)
    # def test_login9(self, dat9):
    #     """验证会员本次积分是否正确"""
    #     print dat9
    #     self.a.login9(dat9['vip'], dat9['barCode'],  dat9['num'])

    @ddt.data(*datadict10)
    def test_login10(self, dat10):
        """验证积分兑换是否跳转"""
        print dat10
        self.a.login10(dat10['vip'], dat10['barCode'],  dat10['num1'])

    @ddt.data(*datadict11)
    def test_login11(self, dat11):
        """验证冻结会员提示"""
        print dat11
        self.a.login11(dat11['vip'], dat11[u'result'])

    @ddt.data(*datadict12)
    def test_login12(self, dat12):
        """验证提示商品已下架"""
        print dat12
        self.a.login12(dat12['vip'], dat12['barCode'], dat12[u'result'])

    @ddt.data(*datadict13)
    def test_login13(self, dat13):
        """验证快捷键跳转"""
        print dat13
        self.a.login13(dat13[u'result1'])

if __name__ == "__main__":
    unittest.main(verbosity=2)