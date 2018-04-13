from HTMLTestRunner import HTMLTestRunner
import time
import unittest

# 定义测试用例的目录为当前目录
test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './reports' + "/" + now + ".html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(discover)




    #runner = unittest.TextTestRunner()
    #runner.run(discover)

