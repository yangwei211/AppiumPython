# coding:utf-8
import unittest
import time
from appium import webdriver
from Page.Base import Base
from Page import cityPage,homePage


class SwitchCity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Base.capabilities)
        self.homePage = homePage.homePage(self.driver)
        self.cityPage = cityPage.cityPage(self.driver)
        time.sleep(3)

    def testSwitchCity(self):
        time.sleep(5)
        cityname = self.homePage.city().text
        #self.cityPage.pagetitle().sendkeys("111")
        # self.cityPage.pagetitle().click()
        self.assertEqual(cityname, "上海")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
