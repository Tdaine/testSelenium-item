# -*- coding: utf-8 -*-
import unittest,csv
import os,sys
import time

#手工添加案例到套件
def createsuite():
    discover=unittest.defaultTestLoader.discover('../testSelenium-Item',pattern='test*.py',top_level_dir=None)
    print discover
    return discover
if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)