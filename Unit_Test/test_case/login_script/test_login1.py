# coding=utf-8


import unittest
import ddt
from test_common import ReadExcel
from test_common import Login_UZG


filepath = "D:\\Unit_Test\\data\\loginTest.xlsx"
sheetName1 = "Sheet1"
sheetName2 = "Sheet2"

datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data()
datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data()
# datadict3 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data(7)


@ddt.ddt
class LoginTest(unittest.TestCase):
    """机构号密码登录测试"""
    a = Login_UZG.OpenUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        self.a.stay_uzg()

    def tearDown(self):
        pass

    @ddt.data(*datadict1)
    def test_login01(self, dat1):

        """机构号输入测试"""
        print str(dat1).decode("unicode_escape").encode("utf8")
        self.a.login1(dat1['username'], dat1['password'], dat1[u'result'])

    @ddt.data(*datadict2)
    def test_login02(self, dat2):
        """密码输入测试"""
        print dat2
        self.a.login2(dat2['username'], dat2['password'], dat2[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)