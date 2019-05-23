# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
import time
from test_common import Storage_package

excelPath = ("D:\\Unit_Test\\data\\shprkTest.xlsx")
sheetName2 = ("Sheet2")
sheetName17 = ("Sheet17")

datadict1 = ReadExcel.ExcelUtil(excelPath, sheetName2).dict_data()
datadict17 = ReadExcel.ExcelUtil(excelPath, sheetName17).dict_data()

@ddt.ddt
class LoginTest (unittest.TestCase):

    a = Storage_package.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        time.sleep(7)
        cls.a.click_storage()
        cls.a.input_shpglframe()
        cls.a.input_shyprkframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        self.a.click_esc()

    @ddt.data(*datadict1)
    def test_storage2(self, dat1):
        """点击没有编码测试"""
        print dat1
        self.a.storage1(dat1['itemname'], dat1['saleprice'], dat1['vipprice'], dat1['purprice'], dat1['purnum'],
                        dat1['expirydate'], dat1['standard'], dat1['marks'], dat1[u'num1'],)

    @ddt.data(*datadict17)
    def test_storage3(self, dat2):
        """点击没有编码测试"""
        print dat2
        self.a.storage17(dat2['itemname'], dat2['saleprice'], dat2['vipprice'], dat2['purprice'], dat2['purnum'],
                         dat2['expirydate'], dat2['standard'], dat2['marks'], dat2[u'num2'],)


if __name__ == "__main__":
    unittest.main(verbosity=2)