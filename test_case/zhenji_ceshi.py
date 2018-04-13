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
    def huigui(self, status, biaoming, money):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print(driver.current_activity)

        if status == 'N':
            time.sleep(4)
            try:
                driver.find_element_by_name("s | 跳过").click()
            except Exception as b:
                print(b)
                time.sleep(10)


            #time.sleep(10)
            print(driver.current_activity)

            """
            driver.find_element_by_name("我的").click()
            print(driver.current_activity)
            #time.sleep(2)
            driver.find_element_by_id("com.jfcaifu.main:id/login_et_phone").clear()
            driver.find_element_by_id("com.jfcaifu.main:id/login_et_phone").send_keys("15821903152")
            driver.keyevent("4")    # 返回键，收回键盘

            driver.find_element_by_id("com.jfcaifu.main:id/login_et_pwd").send_keys("a1234567")
            driver.keyevent("4")    # 返回键，收回键盘

            driver.find_element_by_name("登录").click()
            time.sleep(1)
            """
            print(driver.get_window_size())
            time.sleep(1.5)

            #TouchAction(driver).press(x=100, y=100).move_to(x=250, y=0).wait(50).move_to(x=280, y=0).wait(50).move_to(x=100, y=350).wait(100).release().perform()
            #TouchAction(driver).press(x=400, y=400).wait(6000).perform()  # 第六个
            #TouchAction(driver).press(x=400, y=300).wait(6000).perform()  # 第三个
            #TouchAction(driver).press(x=250, y=300).wait(6000).perform()   # 第二个
            #TouchAction(driver).press(x=150, y=300).wait(6000).perform()   #第一个

            TouchAction(driver).press(x=150, y=300).wait(50).move_to(x=50, y=0).wait(50).move_to(x=150, y=0).wait(100).move_to(x=0, y=100)\
                .wait(100).release().perform()

            try:
                driver.find_element_by_id("com.jfcaifu.main:id/iv_close").click()  # 升级提示弹框
            except Exception as e:
                print(e)
                pass


            driver.find_element_by_name("理财").click()
            time.sleep(0.5)
            time.sleep(1)
            for A in range(20):
                driver.keyevent(20)  # 按下键

            driver.find_element_by_name(biaoming).click()
            driver.find_element_by_name("立即买入").click()
            time.sleep(0.5)
            driver.find_element_by_name("最低投资100元").send_keys(money)
            time.sleep(2)

            
            driver.keyevent("111")  # esc键，收回键盘
            time.sleep(2)
            driver.find_element_by_id("com.jfcaifu.main:id/confirm_payment").click()
            time.sleep(3)


            for A in range(20):
                driver.keyevent(20)  # 按下键

            driver.find_element_by_xpath("//android.widget.EditText").send_keys("Chq199312")
            #time.sleep(3)
            driver.keyevent("111")   # esc键

            driver.find_element_by_xpath("//android.view.View[@content-desc=\'确认 Link\']").click()  # 提交投资
            time.sleep(5)

            driver.find_element_by_name("恭喜您，投资成功")
            """
            if bool(driver.find_element_by_name("恭喜您，投资成功")) == True:
                time.sleep(3)
                driver.find_element_by_id("com.jfcaifu.main:id/bindsuccess_btn").click()"""



















Android().huigui("N", "908测试标", "100")
