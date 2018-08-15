# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
import time
import os, sys
from Public import HTMLTestRunner

# 获取当前py文件路径地址，并进行路径分割（分割成目录路径和文件名称）
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
case_path = dirname + "/TestCase"
result = dirname + "/Result/"
# 获取当前文件目录相对路径
dirpath = os.path.dirname(sys.argv[0])
# 拼接page、public文件目录路径
Page = dirpath + '/Page'
Public = dirpath + '/public'
sys.path.append(Page)
sys.path.append(Public)


def Creatsuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()

    # 定搜索用例文件的方法
    # print case_path
    # from TestCase.Test_Login import Login
    # from TestCase.Test_Search import Search
    # from TestCase.Test_SwitchMeun import SwitchMeun
    # from TestCase.Test_SwitchCity import SwitchCity
    from TestCase.test_Jenkins_CreateItem import TestCreateItem
    from TestCase.test_Jenkins_DeleteItem import TestDeleteItem
    #testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
    #testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Search))
    #testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SwitchMeun))
    #testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SwitchCity))
    testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateItem))
    testunit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteItem))
    '''
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
    print testunit
    return testunit
    '''
    return testunit


test_case = Creatsuite()

# 获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 定义个报告存放路径，支持相对路径
tdresult = result + day

# if os.path.exists(tdresult):  # 检验文件夹路径是否已经存在
#     filename = tdresult + "/" + now + "_result.html"
#     fp = open(filename, 'wb')
#     # 定义测试报告
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title='Appium测试报告',
#                                            description='执行情况：')
#
#     # 运行测试用例
#     runner.run(test_case)
#     fp.close()  # 关闭报告文件
# else:
#     os.mkdir(tdresult)  # 创建测试报告文件夹
#     filename = tdresult + "/" + now + "_result.html"
#     fp = open(filename, 'wb')
#     # 定义测试报告
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title='Appium测试报告',
#                                            description='执行情况：')
#
#     # 运行测试用例
#     runner.run(test_case)
#     fp.close()  # 关闭报告文件

if os.path.exists(tdresult):  # 检验文件夹路径是否已经存在
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='selenium测试报告',
                                           description='执行情况：')

    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
else:
    os.mkdir(tdresult)  # 创建测试报告文件夹
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='selenium测试报告',
                                           description='执行情况：')

    # 运行测试用例
    runner.run(test_case)
    fp.close()  # 关闭报告文件
