# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Storage_inbulk
import os

filepath = "D:\\Unit_Test\\data\\inbulkTest.xlsx"
# filepath = os.getcwd() + ("\\data\\inbulkTest.xlsx")
sheetName7 = ("Sheet7")
sheetName8 = ("Sheet8")
sheetName9 = ("Sheet9")
datadict7 = ReadExcel.ExcelUtil(filepath, sheetName7).dict_data()
datadict8 = ReadExcel.ExcelUtil(filepath, sheetName8).dict_data()
datadict9 = ReadExcel.ExcelUtil(filepath, sheetName9).dict_data()


@ddt.ddt
class InbulkTest(unittest.TestCase,):
    """散货商品上架入库测试"""
    a = Storage_inbulk.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        cls.a.click_storage()
        cls.a.storage_iframe()
        cls.a.stroage_inbulk()
        cls.a.click_inbulk()
        cls.a.click_putaway()

    @classmethod
    def tearDownClass(cls):
        cls.a.storage_free()
        cls.a.storage_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict7)
    def test_inbulk07(self, dat7):
        """上架入库—销售价格输入测试"""
        print dat7
        self.a.storage7(dat7['saleprice'], dat7[u'result'])

    @ddt.data(*datadict8)
    def test_inbulk08(self, dat8):
        """上架入库—上架入库成功提示测试"""
        print dat8
        self.a.storage8(dat8['saleprice'], dat8['vipprice'], dat8['purprice'], dat8['purnum'], dat8[u'result'])

    @ddt.data(*datadict9)
    def test_inbulk09(self, dat9):
        """上架入库—成功后—在入库记录验证测试"""
        print dat9
        self.a.storage9(dat9[u'result'])

if __name__ == "__main__":
    unittest.main(verbosity=2)