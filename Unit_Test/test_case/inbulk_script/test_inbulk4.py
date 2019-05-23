# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Storage_inbulk
import os

filepath = "D:\\Unit_Test\\data\\inbulkTest.xlsx"
# filepath = os.getcwd() + ("\\data\\inbulkTest.xlsx")
sheetName13 = ("Sheet13")
sheetName14 = ("Sheet14")
sheetName15 = ("Sheet15")
sheetName16 = ("Sheet16")
datadict13 = ReadExcel.ExcelUtil(filepath, sheetName13).dict_data()
datadict14 = ReadExcel.ExcelUtil(filepath, sheetName14).dict_data()
datadict15 = ReadExcel.ExcelUtil(filepath, sheetName15).dict_data()
datadict16 = ReadExcel.ExcelUtil(filepath, sheetName16).dict_data()


@ddt.ddt
class InbulkTest(unittest.TestCase,):
    """已上架散货入库测试"""
    a = Storage_inbulk.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        cls.a.click_storage()
        cls.a.storage_iframe()
        cls.a.stroage_inbulk()
        cls.a.click_onsale()
        cls.a.storage_button()

    @classmethod
    def tearDownClass(cls):
        cls.a.storage_free()
        cls.a.storage_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict13)
    def test_inbulk13(self, dat13):
        """散货商品入库—进货单价输入测试"""
        print dat13
        self.a.storage13(dat13['saleprice1'], dat13['purnum1'], dat13[u'result'])

    @ddt.data(*datadict14)
    def test_inbulk14(self, dat14):
        """散货商品入库—进货数量输入测试"""
        print dat14
        self.a.storage14(dat14['saleprice1'], dat14['purnum1'], dat14[u'result'])

    @ddt.data(*datadict15)
    def test_inbulk15(self, dat15):
        """散货商品入库—入库成功提示测试"""
        print dat15
        self.a.storage15(dat15['saleprice1'], dat15['purnum1'], dat15[u'result'])

    @ddt.data(*datadict16)
    def test_inbulk16(self, dat16):
        """散货商品入库—入库成功后—在入库记录验证测试"""
        print dat16
        self.a.storage16(dat16[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)