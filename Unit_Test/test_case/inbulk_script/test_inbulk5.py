# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Storage_inbulk
import os

filepath = "D:\\Unit_Test\\data\\inbulkTest.xlsx"
# filepath = os.getcwd() + ("\\data\\inbulkTest.xlsx")
sheetName17 = ("Sheet17")
sheetName18 = ("Sheet18")
sheetName19 = ("Sheet19")
sheetName20 = ("Sheet20")
datadict17 = ReadExcel.ExcelUtil(filepath, sheetName17).dict_data()
datadict18 = ReadExcel.ExcelUtil(filepath, sheetName18).dict_data()
datadict19 = ReadExcel.ExcelUtil(filepath, sheetName19).dict_data()
datadict20 = ReadExcel.ExcelUtil(filepath, sheetName20).dict_data()


@ddt.ddt
class InbulkTest(unittest.TestCase,):
    """入库记录编辑测试"""
    a = Storage_inbulk.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        cls.a.click_storage()
        cls.a.storage_iframe()
        cls.a.stroage_inbulk()
        cls.a.click_record()
        cls.a.record_edit()

    @classmethod
    def tearDownClass(cls):
        cls.a.storage_free()
        cls.a.storage_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict17)
    def test_inbulk17(self, dat17):
        """入库记录编辑—进货单价输入测试"""
        print dat17
        self.a.storage17(dat17['saleprice2'], dat17['purnum2'], dat17[u'result'])

    @ddt.data(*datadict18)
    def test_inbulk18(self, dat18):
        """入库记录编辑—进货总数输入测试"""
        print dat18
        self.a.storage18(dat18['saleprice2'], dat18['purnum2'], dat18[u'result'])

    @ddt.data(*datadict19)
    def test_inbulk19(self, dat19):
        """入库记录—编辑成功提示测试"""
        print dat19
        self.a.storage19(dat19['saleprice2'], dat19['purnum2'], dat19[u'result'])

    @ddt.data(*datadict20)
    def test_inbulk20(self, dat20):
        """入库记录—编辑成功后—在入库记录中验证测试"""
        self.a.storage20(dat20[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)