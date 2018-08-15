# coding=utf-8
import sys
from common.base import BaseCommon
from common.util import Util
from Public.login import Mylogin
from selenium import webdriver
import unittest
import os
import time
from report import HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf8')


class TestDeleteItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.basecommon = BaseCommon(self.driver)
        self.mlogin = Mylogin(self.driver)
        self.data = Util().operateYaml("../data/jkData/pageData.yaml")  # 取到yaml里边的所有数据
        self.driver.get(self.data['login']['url'])

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.basecommon.screenshot(screen_name)
        self.driver.quit()

    def testJenkins01_02(self):
        time.sleep(2)
        self.mlogin.login()
        print "success......."
        self.taskdata = Util().operateYaml("../data/jkData/newTaskData.yaml")  # 取到yaml里边的所有数据
        self.driver.find_element_by_link_text(self.taskdata['newtask']['newtask_01']['tasktitle']).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(self.taskdata['newtask']['newtask_02']['deletebutton']).click()
        alert1 = self.driver.switch_to.alert
        alert1.accept()


if __name__ == "__main__":
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestDeleteItem("testJenkins01_02"))
    filePath = "../report/" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + "testResult.html"
    fp = file(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report for me', description='This is my Report')
    runner.run(suiteTest)
