# -*- coding: utf-8 -*-
import time

from selenium import webdriver

class TestSearch(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")


    def teardown(self):
        time.sleep(5)
        self.driver.quit()


    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("你好")
        self.driver.find_element_by_id("su").click()