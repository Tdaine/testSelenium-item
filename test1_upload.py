
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
    #上传文件
    def test1_upload(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("filename").clear()
        driver.find_element_by_name("filename").send_keys(u"C:\\Users\\dell\\OneDrive\\Pictures\\a97a7102dab7f1fd.jpg")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.implicitly_wait(30)
        if driver.find_element_by_link_text(u"a97a7102dab7f1fd.jpg").is_displayed():
            print "上传成功"
        else:
            print "上传失败"
        driver.quit()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()