# coding=utf-8
import unittest
import ddt
from test_common import ReadExcel
import time
from test_common import Storage_package

excelPath = ("D:\\Unit_Test\\data\\shprkTest.xlsx")
sheetName3 = ("Sheet3")
sheetName4 = ("Sheet4")
sheetName5 = ("Sheet5")
sheetName6 = ("Sheet6")

datadict1 = ReadExcel.ExcelUtil(excelPath, sheetName3).dict_data()
datadict2 = ReadExcel.ExcelUtil(excelPath, sheetName4).dict_data()
datadict3 = ReadExcel.ExcelUtil(excelPath, sheetName5).dict_data()
datadict4 = ReadExcel.ExcelUtil(excelPath, sheetName6).dict_data()


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
    def test_storage4(self, dat1):
        """保质期验证,判断保质期很短，请选择保质期"""
        print dat1
        self.a.storage2(dat1['expirydate'], dat1[u'num3'])

    @ddt.data(*datadict2)
    def test_storage5(self, dat2):
        """保质期验证，请选择保质期,验证年份"""
        print dat2
        self.a.storage3(dat2['expirydate'], dat2[u'num4'])

    @ddt.data(*datadict3)
    def test_storage6(self, dat3):
        """保质期验证，请选择保质期,验证月份"""
        print dat3
        self.a.storage4(dat3['expirydate'], dat3[u'num4'])

    @ddt.data(*datadict4)
    def test_storage7(self, dat4):
        """保质期验证，保质期很短，请选择保质期,验证月份"""
        print dat4
        self.a.storage5(dat4['expirydate'], dat4[u'num3'])


if __name__ == "__main__":
    unittest.main(verbosity=2)