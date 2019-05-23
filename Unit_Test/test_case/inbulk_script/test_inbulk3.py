# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Storage_inbulk
import os

filepath = "D:\\Unit_Test\\data\\inbulkTest.xlsx"
# filepath = os.getcwd() + ("\\data\\inbulkTest.xlsx")
sheetName10 = ("Sheet10")
sheetName11 = ("Sheet11")
sheetName12 = ("Sheet12")
datadict10 = ReadExcel.ExcelUtil(filepath, sheetName10).dict_data()
datadict11 = ReadExcel.ExcelUtil(filepath, sheetName11).dict_data()
datadict12 = ReadExcel.ExcelUtil(filepath, sheetName12).dict_data()


@ddt.ddt
class InbulkTest(unittest.TestCase, ):
    """编辑散货测试"""
    a = Storage_inbulk.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        cls.a.click_storage()
        cls.a.storage_iframe()
        cls.a.stroage_inbulk()
        cls.a.click_onsale()
        cls.a.click_edit()

    @classmethod
    def tearDownClass(cls):
        cls.a.storage_free()
        cls.a.storage_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict10)
    def test_inbulk10(self, dat10):
        """编辑散货—商品名称输入测试"""
        print dat10
        self.a.storage10(dat10['itemname'], dat10[u'result'])

    @ddt.data(*datadict11)
    def test_inbulk11(self, dat11):
        """编辑散货—销售价格输入测试"""
        print dat11
        self.a.storage11(dat11['itemname'], dat11['saleprice'], dat11[u'result'])

    @ddt.data(*datadict12)
    def test_inbulk12(self, dat12):
        """编辑散货—编辑成功测试"""
        print dat12
        self.a.storage12(dat12['itemname'], dat12['saleprice'], dat12['vipprice'], dat12['standard'], dat12[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)