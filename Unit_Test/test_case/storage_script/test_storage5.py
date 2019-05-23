# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
import time
from test_common import Storage_package

excelPath = ("D:\\Unit_Test\\data\\shprkTest.xlsx")
sheetName10 = ("Sheet10")

datadict1 = ReadExcel.ExcelUtil(excelPath, sheetName10).dict_data()

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
    def test_storage10(self, dat1):
        """删除入库记录"""
        print dat1
        self.a.storage9(dat1[u'num2'], dat1[u'num1'])

    # @ddt.data(*datadict1)
    # def test_storage2(self, dat2):
    #     print dat2
    #     self.a.storage10(dat2[u'num2'], dat2[u'num1'])


if __name__ == "__main__":
    unittest.main(verbosity=2)