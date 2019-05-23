# coding=utf-8

import unittest
import ddt
import time
from test_common import ReadExcel
from test_common import Storage_package

excelPath = ("D:\\Unit_Test\\data\\shprkTest.xlsx")
sheetName1 = ("Sheet1")
sheetName16 = ("Sheet16")

datadict1 = ReadExcel.ExcelUtil(excelPath, sheetName1).dict_data()
#datadict16 = ReadExcel.ExcelUtil(excelPath, sheetName16).dict_data()


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
    def test_storage1(self, dat1):
        """自定义编码入库"""
        print dat1
        self.a.storage(dat1['itemcode'], dat1['itemname'], dat1['saleprice'], dat1['vipprice'], dat1['purprice'], dat1['purnum'],
                       dat1['expirydate'], dat1['standard'], dat1['marks'], dat1[u'num1'],)

    # @ddt.data(*datadict16)
    # def test_storage2(self, dat2):
    #     print dat2
    #     self.a.storage16(dat2['itemcode'], dat2['itemname'], dat2['saleprice'], dat2['vipprice'],dat2['purprice'],dat2['purnum'],
    #                      dat2['expirydate'], dat2['standard'], dat2['marks'], dat2[u'num2'],)

if __name__ == "__main__":
    unittest.main(verbosity=2)