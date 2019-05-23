# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Checkstand_package1


filepath = ("D:\\Unit_Test\\data\\checkstandTest.xlsx")
sheetName4 = ("Sheet4")
sheetName5 = ("Sheet5")
sheetName6 = ("Sheet6")
sheetName7 = ("Sheet7")
sheetName8 = ("Sheet8")


datadict4 = ReadExcel.ExcelUtil(filepath, sheetName4).dict_data()
datadict5 = ReadExcel.ExcelUtil(filepath, sheetName5).dict_data()
datadict6 = ReadExcel.ExcelUtil(filepath, sheetName6).dict_data()
datadict7 = ReadExcel.ExcelUtil(filepath, sheetName7).dict_data()
datadict8 = ReadExcel.ExcelUtil(filepath, sheetName8).dict_data()


@ddt.ddt
class LoginTest (unittest.TestCase):

    a = Checkstand_package1.shyt()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.click_shyt()
        cls.a.input_shytiframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
       self.a.click_lastCountUl()

    @ddt.data(*datadict4)
    def test_login4(self, dat4):
        """免一元内零头结算"""
        print dat4
        self.a.login4(dat4['vip'], dat4['barCode'], dat4[u'str1'], dat4[u'str2'], dat4[u'str3'], dat4[u'str4'])

    @ddt.data(*datadict5)
    def test_login5(self, dat5):
        """免十元内零头结算"""
        print dat5
        self.a.login5(dat5['vip'], dat5['barCode'], dat5[u'str1'], dat5[u'str2'], dat5[u'str3'], dat5[u'str4'])

    @ddt.data(*datadict6)
    def test_login6(self, dat6):
        """赊账结算"""
        print dat6
        self.a.login6(dat6['vip'], dat6['barCode'], dat6['payM'], dat6[u'str1'], dat6[u'str2'], dat6[u'str3'], dat6[u'str4'])

    @ddt.data(*datadict7)
    def test_login6(self, dat7):
        """十元内零头减免加赊账结算"""
        print dat7
        self.a.login7(dat7['vip'], dat7['barCode'], dat7['payM'], dat7[u'str1'], dat7[u'str2'], dat7[u'str3'], dat7[u'str4'])

    @ddt.data(*datadict8)
    def test_login7(self, dat8):
        """一元内零头减免加赊账结算"""
        print dat8
        self.a.login8(dat8['vip'], dat8['barCode'], dat8['payM'], dat8[u'str1'], dat8[u'str2'], dat8[u'str3'], dat8[u'str4'])

if __name__ == "__main__":
    unittest.main(verbosity=2)