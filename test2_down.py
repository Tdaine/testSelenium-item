# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re, os

class Testupload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080"
        self.verificationErrors = []
        self.accept_next_alter = True

    #下载文件
    def test2_down(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"a97a7102dab7f1fd.jpg").click()
        driver.implicitly_wait(30)
        if os.path.exists(u"C:\\Users\\dell\\OneDrive\\Pictures\\a97a7102dab7f1fd.jpg"):
            print "Download successfully"
        else:
            print "Download Failed"
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([],self.verificationErrors)

if __name__=="__name__":
    unittest.main()