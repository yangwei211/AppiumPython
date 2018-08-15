# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
import time
from appium import webdriver


class Base():
    capabilities = {'platformName': 'Android',
                    'platformVersion': '5.0',
                    'deviceName': 'samsung-sm_n9002-a7a564f9',
                    'appPackage': 'com.guokr.mentor',
                    'appActivity': '.ui.activity.MainActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)


driver = Base().driver
