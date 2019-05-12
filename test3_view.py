# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os
class Testupload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    #查看文件
    def test3_view(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath(u"/html/body/div[3]/table/tbody/tr[1]/td[7]/a[1]").click()
        driver.implicitly_wait(30)
        handles = driver.window_handles #获取当前打开的所有窗口的句柄
        print(handles)
        driver.switch_to.window(handles[1]) #切换到第二个窗口的句柄
        print(driver.current_window_handle)
        print(driver.title)
        print(driver.current_url)
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()