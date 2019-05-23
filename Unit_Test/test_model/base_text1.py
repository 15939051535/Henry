#coding=utf-8

from selenium import webdriver
import unittest
import ddt
from test_common import ReadExcel
from test_model import base_text


APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  #定义邮掌柜路径
login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html") #定义登录页面file文件路径

options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH



filepath = "D:\\Unit_Test\\data\\loginTest.xlsx"
sheetName1 = "Sheet1"
sheetName2 = "Sheet2"
datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data()
datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data()


'''机构号密码登录测试'''
@ddt.ddt
class LoginTest(unittest.TestCase,):


    @classmethod
    def setUpClass(cls):
        cls.a = base_text.OpenUZG()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        self.a.stay_uzg()

    def tearDown(self):
        pass

    '''机构号输入框提示判定'''
    @ddt.data(*datadict1)
    def test_login1(self, dat1):
        print dat1
        self.a.login1(dat1['username'], dat1['password'], dat1[u'result'])

    # '''密码输入框提示判定'''
    # @ddt.data(*datadict2)
    # def test_login2(self, dat2):
    #     print dat2
    #     self.a.login2(dat2['username'], dat2['password'], dat2[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)