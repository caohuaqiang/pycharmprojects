#coding=utf-8
import time
import threading
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '4782e003'
desired_caps['appPackage'] = 'com.jfcaifu.main'
desired_caps['appActivity'] = 'com.rd.app.activity.LoginingAct'





class Android():
    # 获取屏幕宽和高
    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print(x, y)
        return (x, y)



    # 向左滑动（t为持续时间）
    def swipeLeft(self, driver, t):
        I = Android().getSize(driver)
        x1 = int(I[0]*0.75)
        y1 = int(I[1]*0.5)
        x2 = int(I[0]*0.25)
        driver.swipe(x1, y1, x2, y1, t)



    # 向右滑动
    def swipeRight(self, driver, t):
        l = Android().getSize(driver)
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        driver.swipe(x1, y1, x2, y1, t)



    # 向上滑动
    def swipeUp(self, driver, t):
        l = Android().getSize(driver)
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.85)
        y2 = int(l[1] * 0.01)
        driver.swipe(x1, y1, x1, y2, t)



    # 向下滑动
    def swipeDown(self, driver, t):
        l = Android().getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        driver.swipe(x1, y1, x1, y2, t)







    def huigui(self, status, biaoming, money, type):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print(driver.current_activity)


        # 刚装好没登陆过为Y，已登陆过为N
        if status == 'Y':
            driver.find_element_by_name("我的").click()
            time.sleep(5)
            driver.find_element_by_name("请输入手机号").send_keys("15821903152")
            driver.find_element_by_id("com.jfcaifu.main:id/login_et_pwd").send_keys("a15821903152")
            print(driver.current_activity)
            driver.find_element_by_name("登录").click()
            print(driver.current_activity)
            TouchAction(driver).press(x=200, y=600).move_to(x=250, y=0).wait(50).move_to(x=280, y=0).wait(50).move_to(
                x=100, y=350).wait(100).release().perform()
            TouchAction(driver).press(x=200, y=600).move_to(x=250, y=0).wait(50).move_to(x=280, y=0).wait(50).move_to(
                x=100, y=350).wait(100).release().perform()


        if status == 'N':
            time.sleep(1)
            print(driver.current_activity)
            #TouchAction(driver).press(x=200, y=600).wait(10000).perform()    # 第一个
            TouchAction(driver).press(x=200, y=600).move_to(x=250, y=0).wait(100).move_to(x=300, y=0).wait(100).move_to(x=100, y=350).wait(500).release().perform()

        try:
            driver.find_element_by_id("com.jfcaifu.main:id/iv_close").click()       # 升级提示弹框
        except Exception as e:
            print(e)
            pass


        driver.find_element_by_id("com.jfcaifu.main:id/main_iv_list").click()   # 理财
        time.sleep(1)
        for A in range(20):
            driver.keyevent(20)     # 按下键
        #Android().swipeUp(driver, 20000)
        driver.find_element_by_name(biaoming).click()
        time.sleep(0.5)
        driver.find_element_by_name("立即买入").click()
        time.sleep(0.5)
        driver.find_element_by_name("最低投资100元").send_keys(money)

        # 福利选择
        if type == "redpacket":
            driver.find_element_by_name("请选择可用红包").click()
            time.sleep(0.5)
            driver.find_element_by_name("回归红包-1元").click()
            driver.find_element_by_name("确定").click()


        if type == "coupon":
            driver.find_element_by_name("加息券").click()
            time.sleep(0.5)
            driver.find_element_by_name("杜兵全程百分之1").click()
            driver.find_element_by_name("确定").click()


        if type == "fanxian":
            driver.find_element_by_name("参加大额投资返现红包").click()


        driver.find_element_by_name("确定").click()
        time.sleep(0.5)





t1 = threading.Thread(target=Android().huigui, args=("N", "回归测试用标-60天02", "10000", "fanxian"))

t1.start()





















