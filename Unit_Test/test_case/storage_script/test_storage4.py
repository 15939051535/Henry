# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
import time
from test_common import Storage_package


excelPath = ("D:\\Unit_Test\\data\\shprkTest.xlsx")
sheetName7 = ("Sheet7")
sheetName8 = ("Sheet8")
sheetName9 = ("Sheet9")

datadict1 = ReadExcel.ExcelUtil(excelPath, sheetName7).dict_data()
datadict2 = ReadExcel.ExcelUtil(excelPath, sheetName8).dict_data()
datadict3 = ReadExcel.ExcelUtil(excelPath, sheetName9).dict_data()


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
        pass

    @ddt.data(*datadict1)
    def test_storage8(self, dat1):
        """删除供应商测试"""
        print dat1
        self.a.storage6(dat1['itemname'], dat1['saleprice'], dat1['purprice'], dat1['purnum'], dat1[u'num2'], dat1[u'num1'])

    @ddt.data(*datadict2)
    def test_storage9(self, dat2):
        """修改供应商测试"""
        print dat2
        self.a.storage7(dat2['itemname'], dat2['saleprice'], dat2['purprice'], dat2['purnum'],
                        dat2['editIpt'], dat2[u'num1'])

    # @ddt.data(*datadict3)
    # def test_storage3(self, dat3):
    #     print dat3
    #     self.a.storage7(dat3['itemname'], dat3['saleprice'], dat3['purprice'], dat3['purnum'],
    #                     dat3['editIpt'], dat3[u'num1'])

if __name__ == "__main__":
    unittest.main(verbosity=2)