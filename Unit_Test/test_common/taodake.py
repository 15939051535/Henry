# coding=utf-8

from selenium import webdriver
import time
import Wait_Time
from test_base import base_pack


class ForTt(object):

    t = Wait_Time.Ttime()


    def open_uzg(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.chaxinyu.net/p.php/52l.html")
        self.driver.maximize_window()
        self.b = base_pack.BasePack(self.driver)

    def forget_iframe(self):
        loc = ("id", "wwwchaxinyunet_iframepage")
        self.b.switch_iframe(loc)

    def forget_free(self):
        self.driver.switch_to.default_content()

    def next_step(self):
        self.driver.find_element_by_xpath("//div[@class='drop_sub']/input").send_keys(
            "https://detail.tmall.com/item.htm?id=563037197945")
        self.driver.find_element_by_xpath("//div[@id='tbbox']/ul[1]/button").click()

    def get_code2(self):
        text1 = self.driver.find_element_by_xpath("//div[@class='ct_result fl']/div[0]").text
        text2 = self.driver.driver.find_element_by_xpath("//div[@class='ct_result fl']/div[1]").text
        print(text1)
        print(text2)

if __name__ == "__main__":
    a = ForTt()
    a.open_uzg()
    time.sleep(2)
    a.forget_iframe()
    time.sleep(2)
    a.next_step()
    time.sleep(2)
    a.get_code2()
    time.sleep(2)
    a.forget_free()
    driver.quit()
