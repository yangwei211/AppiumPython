# coding=utf-8
from appium import webdriver
import time


class Base():
    '''desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.guokr.mentor'  # 'com.nicksong.toastutil'#
    desired_caps['appActivity'] = '.ui.activity.MainActivity'  # '.MainActivity'
    desired_caps['newCommandTimeout'] = 180  # 设置超时时间
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    '''

    capabilities = {'platformName': 'Android',
                    'platformVersion': '6.0.1',
                    'deviceName': 'samsung-sm_n9300-a7a564f9',
                    'appPackage': 'com.guokr.mentor',
                    'appActivity': '.ui.activity.MainActivity',
                    'newCommandTimeout': '180',
                    'sessionOverride': 'true',
                    # 'unicodeKeyboard':True,
                    # 'resetKeyboard':True,
                    }
    # driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

# driver = Base().driver
