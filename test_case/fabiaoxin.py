# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading


class FB():
    def fabiao(self, biaoming, hongbaofangan, jiaxiquanfangan, yunyingfangan, jine, lilv, tianshu, xianshijiaxi):
        for A in range(1):
            chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
            driver = webdriver.Firefox()
            driver.implicitly_wait(20)
            driver.get("https://erp-t.jfcaifu.com/admin/login.html")
            driver.maximize_window()
            #time.sleep(3)
            #登录
            try:
                driver.find_element_by_id("userName").clear()
                driver.find_element_by_id("userName").send_keys("admin")
                driver.find_element_by_id("password").clear()
                driver.find_element_by_id("password").send_keys("123456")
                driver.find_element_by_id("valicode").clear()
                driver.find_element_by_id("valicode").send_keys("jfcf")

                driver.find_element_by_xpath("html/body/div[1]/div/form/ul/li[5]/input").click()

                time.sleep(1)
                driver.find_element_by_xpath(".//*[@id='nav']/div[3]/div[1]/div[1]").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div/div[5]/div/div/div[3]/div[2]/ul/li/div/a/span").click() #借款初审
                time.sleep(1)
                iframe_jiekuanchushen = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/iframe"
                driver.switch_to.frame(driver.find_element_by_xpath(iframe_jiekuanchushen))        #跳转到借款初审页面的iframe框架内
                driver.find_element_by_id("a").click()  #发标
                #driver.switch_to.default_content() #跳出iframe
                time.sleep(1)
                iframe_tankuang = "/html/body/div[3]/div[2]/iframe"
                driver.switch_to.frame(driver.find_element_by_xpath(iframe_tankuang))      #跳转到弹框页面(ifram嵌套，从第一层跳到第二层)


                #driver.find_element_by_xpath("html/body/form/div[1]/div/div[3]/i").click()  # 活动标
                driver.find_element_by_xpath("/html/body/form/div/div/div[2]/i").click()    # 热销中

                driver.find_element_by_id("ads").send_keys(biaoming) #标名
                driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div/input").send_keys("CHQ888") #项目编号



                driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div/input").click()  #弹出红包方案下拉框
                time.sleep(0.5)
                B = '//*[@lay-value="'+hongbaofangan+'"]'
                driver.find_element_by_xpath(B).click()   #选择红包方案(传参)
                #和这个相同：driver.find_element_by_xpath("//*[@lay-value='chq大转盘红包方案']").click()


                driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div/div/div/input").click() #弹出加息券方案下拉框
                time.sleep(0.5)
                C = '//*[@lay-value="'+jiaxiquanfangan+'"]'
                driver.find_element_by_xpath(C).click()   #选择加息券方案（传参）






                """
                driver.find_element_by_xpath("//*[@placeholder='请选择运营活动']").click() #弹出运营活动方案下拉框
                time.sleep(0.5)
                D = '//*[@lay-value="'+yunyingfangan+'"]'
                driver.find_element_by_xpath(D).click()  # 选择运营活动方案
                """


                # print(driver.find_element_by_xpath('//*[@title="大额返现双11版"]').is_displayed())
                driver.find_element_by_xpath('html/body/form/div[4]/div/div[1]/span').click()       #第一个运营活动
                driver.find_element_by_xpath('html/body/form/div[4]/div/div[2]/span').click()       # 第二个运营活动
                driver.find_element_by_xpath('html/body/form/div[4]/div/div[3]/span').click()       # 第三个运营活动



                driver.find_element_by_id("account").send_keys(jine)      # 标的金额
                driver.find_element_by_id("apr").send_keys(lilv)  # 年利率
                driver.find_element_by_id("timeLimit").send_keys(tianshu)  # 标的天数

                #driver.find_element_by_id("showIncreaseRate").send_keys(xianshijiaxi)  # 显示加息
                driver.find_element_by_id("putStartTime").click()  # 开标时间
                driver.find_element_by_xpath(".//*[@id='laydate_ok']").click()
                time.sleep(0.5)



                driver.find_element_by_xpath("//*[@placeholder='请选择客服']").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@lay-value='kefu123']").click()  # 客服





                driver.find_element_by_xpath('//*[@placeholder="请选择借款人邮箱"]').click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@lay-value='745133655@qq.com']").click()   # 借款人




                





                #driver.find_element_by_xpath("//*[@placeholder='请选择标的活动图']").click()
                #driver.find_element_by_xpath("//*[@lay-value='41']").click()  # 标的图选择

                #driver.find_element_by_name("content").send_keys("xxxxxxx")  # 借款描述



                driver.find_element_by_xpath("//*[@lay-filter='save']").click()  # 确定，创建标完成

                driver.switch_to.frame(
                    driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div[2]/div/iframe"))
                above = driver.find_element_by_xpath(".//*[@id='datagrid-row-r1-2-0']/td[11]/div")
                ActionChains(driver).move_to_element(above).perform()  # 悬停在“操作栏”，展开选项
                time.sleep(2)
                driver.find_element_by_xpath(
                    ".//*[@id='datagrid-row-r1-2-0']/td[11]/div/dl/dt/a").click()  # 悬停展开的选项中，选择【初审】
                # 以下为审核标的页面
                driver.switch_to.default_content()
                time.sleep(1)

                driver.find_element_by_xpath(
                    ".//*[@id='form']/div[1]/div/input[2]").click()  # 是否通过：选择“是”（将标设为通过状态，可进行投资）
                time.sleep(1)

                driver.find_element_by_link_text(u"确定").click()
                time.sleep(3)
                driver.find_element_by_link_text(u"确定").click()  # 关闭弹窗：操作成功！
                driver.quit()




            except Exception as a:
                print(a)
                time.sleep(2)
                #driver.close()






class touzi():
    def wap_touzi(self, username, password, biaoming, money, jiaoyimima):
        for A in range(1):
            try:
                chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
                driver = webdriver.Chrome(chromedriver)
                driver.get(
                    "https://www-t.jfcaifu.com///wap/user/login.html?timeout=1&redirectURL=%2Fwap%2Fmember%2Faccount.html")

                driver.find_element_by_id("phone").send_keys(username)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_partial_link_text("登录").click()
                time.sleep(1)
                driver.find_element_by_partial_link_text("理财").click()
                time.sleep(1)
                js = "window.scrollTo(0,1000)"
                driver.execute_script(js)
                driver.find_element_by_partial_link_text(biaoming).click()
                driver.find_element_by_partial_link_text("立即买入").click()
                time.sleep(1)
                driver.find_element_by_id("buyMoney").send_keys(money)


                """
                driver.find_element_by_xpath("html/body/div[2]/div[6]").click()  # 打开红包选择列表
                time.sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/ul/li/div[2]/div/div/span").click()  # 红包列表的第一个红包
                driver.find_element_by_xpath(".//*[@id='redpacket_list']/div[4]/a").click()  # 确定选择-红包
                """

                """
                driver.find_element_by_xpath("html/body/div[2]/div[7]").click()  # 打开加息券选择列表
                time.sleep(1)
                driver.find_element_by_xpath("//*[@class='Coupon_hb_right']").click()  # 加息券列表的第一张加息券
                driver.find_element_by_xpath(".//*[@id='redpacket_list']/div[4]/a").click()  # 确定选择-加息券
                """


                #driver.find_element_by_xpath("html/body/div[2]/div[8]").click()     # 选择大额返现


                driver.find_element_by_xpath("html/body/div[3]/a").click()          # 确定-提交购买

                time.sleep(2)
                driver.find_element_by_xpath("//*[@pname='TransPwd']").send_keys(jiaoyimima)  # 汇付交易密码
                driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/div/a/span").click()  # 确认






            except Exception as a:
                print(a)
                time.sleep(3)
                driver.close()







    def PC_touzi(self, user, password, biaoming, money, jiaoyimima, type):
        for C in range(1):
            try:
                chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
                driver = webdriver.Chrome(chromedriver)
                driver.implicitly_wait(10)
                driver.get("https://www-p.jfcaifu.com///user/login.html")
                driver.maximize_window()
                driver.find_element_by_id("username").send_keys(user)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys("jfcf")
                driver.find_element_by_id("loginOperate").click()
                time.sleep(1)
                driver.find_element_by_partial_link_text("投资广场").click()

                #driver.find_element_by_xpath("//*[@buttoncode='BT020010001']").click()  # 新手标
                driver.find_element_by_xpath("//*[@buttoncode='BT020010002']").click()  # 热销中
                #driver.find_element_by_xpath("//*[@buttoncode='BT020010003']").click()  # 活动标

                time.sleep(1)
                driver.find_element_by_partial_link_text(biaoming).click()
                time.sleep(1)
                driver.find_element_by_id("money").send_keys(money)


                # 以下是选择福利类型（传参type）
                if type == "redpacket":
                    driver.find_element_by_xpath("//*[@title='我的红包']").click()
                    time.sleep(0.5)
                    driver.find_element_by_xpath(".//*[@id='redPacketList']/li/div/div/div[2]").click()  # 选择红包列表的第一个红包
                    driver.find_element_by_partial_link_text("确定").click()  # 确认选中红包


                if type == "coupon":
                    driver.find_element_by_xpath("//*[@ title='我的加息券']").click()
                    time.sleep(0.5)
                    driver.find_element_by_xpath(
                        ".//*[@id='couponPacketList']/li/div/div/div[2]").click()  # 加息券列表的第一个加息券
                    driver.find_element_by_id("couponPacketConfirm").click()  # 确认选中加息券



                if type == "fanxian":
                    driver.find_element_by_xpath("//*[@title='参与大额返现']").click()  # 大额返现



                if type == "null":
                    pass






                """
                driver.find_element_by_xpath("//*[@title='我的红包']").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='redPacketList']/li/div/div/div[2]").click()  # 选择红包列表的第一个红包
                driver.find_element_by_partial_link_text("确定").click()   # 确认选中红包
                



                driver.find_element_by_xpath("//*[@ title='我的加息券']").click()
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='couponPacketList']/li/div/div/div[2]").click()  # 加息券列表的第一个加息券
                driver.find_element_by_id("couponPacketConfirm").click()  # 确认选中加息券



                driver.find_element_by_xpath("//*[@title='参与大额返现']").click()   # 大额返现
                """
                D = driver.window_handles  # 投资页面
                print(D)
                driver.find_element_by_xpath("//*[@value='立即购买']").click()

                E = driver.window_handles  # 投资页面+汇付页面
                print(E)
                for i in E:
                    if i not in D:
                        driver.switch_to.window(i)

                print(driver.current_window_handle)
                driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/dl/dd[2]/div[2]/input").send_keys(jiaoyimima)
                driver.find_element_by_partial_link_text("确认").click()
                time.sleep(10)
                driver.quit()






            except Exception as a:
                print(a)
                time.sleep(2)
                driver.close()







class tixian():
    def wap_tixian(self, username, password, money, jiaoyimima):
        for A in range (1):
            chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver)
            driver.implicitly_wait(5)
            try:
                driver.get("https://www-t.jfcaifu.com//wap/user/login.html?timeout=1&redirectURL=%2Fwap%2Fmember%2Faccount.html")
                driver.find_element_by_id("phone").send_keys(username)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_partial_link_text("登录").click()
                time.sleep(0.5)
                driver.find_element_by_partial_link_text("提现").click()
                driver.find_element_by_id("input-money").send_keys(money)
                driver.find_element_by_partial_link_text("下一步").click()
                time.sleep(0.5)
                driver.find_element_by_partial_link_text("下一步").click()
                driver.find_element_by_partial_link_text("确定").click()
                driver.find_element_by_id("TransPwd").send_keys(jiaoyimima)
                driver.find_element_by_partial_link_text("确定").click()   # 提交
                driver.find_element_by_partial_link_text("确定").click()


            except Exception as a:
                print(a)


            finally:
                time.sleep(2)
                driver.close()




    def PC_tixian(self, user, password, money, jiaoyimima):
        for A in range(1):
            try:
                chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
                driver = webdriver.Chrome(chromedriver)
                driver.implicitly_wait(5)
                driver.maximize_window()
                driver.get("https://www-t.jfcaifu.com/user/login.html")
                driver.find_element_by_id("username").send_keys(user)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys("jfcf")
                driver.find_element_by_id("loginOperate").click()
                time.sleep(0.5)
                driver.find_element_by_partial_link_text("提现").click()
                time.sleep(0.5)
                B = driver.window_handles
                print(B)
                driver.find_element_by_id("money").send_keys(money)
                driver.find_element_by_id("submitCash").click()    # 确认提现
                time.sleep(0.5)
                C = driver.window_handles
                print(C)
                for huifuyemian in C:
                    if huifuyemian not in B:
                        driver.switch_to.window(huifuyemian)

                driver.find_element_by_id("passWord").send_keys(jiaoyimima)
                driver.find_element_by_partial_link_text("确定").click()
                print(driver.current_window_handle)



            except Exception as a:
                print(a)




            finally:
                driver.close()










class youhui():
    def fahongbao(self, phone, hongbaozhonglei, youxiaotianshu, remark):
        for A in range(1):
            chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver)
            driver.implicitly_wait(5)
            driver.get("https://erp-t.jfcaifu.com/admin/login.html")
            driver.maximize_window()
            try:
                driver.find_element_by_id("userName").send_keys("admin")
                driver.find_element_by_id("password").send_keys("123456")
                driver.find_element_by_id("valicode").send_keys("jfcf")
                driver.find_element_by_xpath("html/body/div[1]/div/form/ul/li[5]/input").click()
                driver.find_element_by_xpath(".//*[@id='topNav']/a[2]").click()   # 增值功能管理
                driver.find_element_by_xpath(".//*[@id='nav']/div[2]/div[1]/div[1]").click()    # 红包管理
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='nav']/div[2]/div[2]/ul/li[5]/div/a/span").click()   # 发红包
                time.sleep(0.5)
                driver.switch_to.frame(driver.find_element_by_xpath("//*[@scrolling='auto']"))   # iframe跳转
                driver.find_element_by_xpath("//*[@placeholder='输入用户名进行搜索']").send_keys(phone)
                driver.find_element_by_xpath("//*[@title='查询']").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@name='ck']").click()   # 勾选
                driver.find_element_by_partial_link_text("发红包").click()
                driver.switch_to.default_content()  # 跳出iframe
                hongbaoxialakuang = driver.find_element_by_xpath("//*[@name='packetCode']")
                Select(hongbaoxialakuang).select_by_visible_text(hongbaozhonglei)     # 选择红包种类
                driver.find_element_by_name("packetDays").send_keys(youxiaotianshu)
                #driver.find_element_by_name("packetRemark").send_keys(remark)  # 备注


                driver.find_element_by_css_selector(".l-btn").click()       # css 提交
                #driver.find_element_by_xpath("//*[@class='l-btn']").click()     # 提交
                driver.find_element_by_partial_link_text("确定").click()
                driver.close()


            except Exception as Z:
                print(Z)
                time.sleep(2)
                driver.close()




    def fajiaxiquan(self, phone, jiaxiquanzhonglei, remark):
        for A in range(1):
            chromedriver = "C:\\Users\Administrator.cu-PC.000\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver)
            driver.implicitly_wait(5)
            driver.maximize_window()
            driver.get("https://erp-t.jfcaifu.com/admin/login.html")
            try:
                driver.find_element_by_id("userName").send_keys("admin")
                driver.find_element_by_id("password").send_keys("123456")
                driver.find_element_by_id("valicode").send_keys("jfcf")
                driver.find_element_by_xpath("html/body/div[1]/div/form/ul/li[5]/input").click()
                driver.find_element_by_xpath(".//*[@id='topNav']/a[2]").click()  # 增值功能管理
                driver.find_element_by_xpath(".//*[@id='nav']/div[5]/div[1]/div[1]").click()    # 加息券管理
                time.sleep(0.5)
                driver.find_element_by_xpath(".//*[@id='nav']/div[5]/div[2]/ul/li[5]/div/a/span").click()   # 发加息券
                time.sleep(0.5)
                driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div[2]/div/iframe"))
                driver.find_element_by_name("searchName").send_keys(phone)
                driver.find_element_by_partial_link_text("查询").click()
                time.sleep(0.5)
                driver.find_element_by_name("ck").click()
                driver.find_element_by_link_text("发加息券").click()
                driver.switch_to.default_content()
                jiaxiquanxialakuang = driver.find_element_by_name("couponCode")
                Select(jiaxiquanxialakuang).select_by_visible_text(jiaxiquanzhonglei)   # 选择加息券种类
                driver.find_element_by_id("couponRemark").send_keys(remark)
                driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/a").click()   # 提交
                driver.find_element_by_partial_link_text("确定").click()
                driver.close()


            except Exception as a:
                print(a)
                time.sleep(2)
                driver.close()














t1 = threading.Thread(target=touzi().wap_touzi, args=("15821903152", "a1234567", "chq0904-90天标02", "1600", "Chq199312"))



t20 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "super20天02", "2000", "Chq199312", "null"))
t21 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "QQQ标30天01", "1060", "Chq199312", "null"))
t22 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "HHH标90天03", "107", "Chq199312", "null"))
t23 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "HHH标90天04", "108", "Chq199312", "null"))
t24 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "HHH标90天05", "109", "Chq199312", "null"))



t31 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "QQQ标20天01", "1000", "a1234567", "null"))
t32 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "QQQ标30天01", "1010", "a1234567", "null"))
t33 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "HHH标90天03", "102", "a1234567", "null"))
t34 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "HHH标90天04", "103", "a1234567", "null"))
t35 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "HHH标90天05", "104", "a1234567", "null"))







t300 = threading.Thread(target=FB().fabiao, args=("chq专属多活动飞翔标", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1000000", "10", "41", "0.5"))
t301 = threading.Thread(target=FB().fabiao, args=("放款测试标02", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1500000", "10", "39", "0.5"))
t302 = threading.Thread(target=FB().fabiao, args=("放款测试标03", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1500000", "10", "39", "0.5"))
t303 = threading.Thread(target=FB().fabiao, args=("放款测试标04", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1500000", "10", "39", "0.5"))
t304 = threading.Thread(target=FB().fabiao, args=("放款测试标05", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1500000", "10", "39", "0.5"))

# t4 = threading.Thread(target=FB().fabiao, args=("1215测试标30天07", "chq大转盘红包方案", "邀请好友方案", "AC20171106150947", "1500000", "10", "30", "0.5"))
# AC20171106150947代表大额返现，AC20171030115936代表双11活动,(-t 大额返现)


t60 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "放款测试标05", "100", "Chq199312", "null"))
t70 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a1234567", "放款测试标05", "100", "a1234567", "null"))
t80 = threading.Thread(target=touzi().PC_touzi, args=("13564809890", "a1234567", "放款测试标05", "100", "qwer1234", "null"))

t90 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "丢雷老母四", "100", "Chq199312", "null"))
t100 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "丢雷老母五", "100", "Chq199312", "null"))





t8 = threading.Thread(target=youhui().fajiaxiquan, args=("13876767676", "杜兵全程百分之1", "备注"))
t9 = threading.Thread(target=tixian().wap_tixian, args=("15821903152", "a1234567", "101", "Chq199312"))
t7 = threading.Thread(target=tixian().PC_tixian, args=("15821903152", "a1234567", "300", "Chq199312"))



t10 = threading.Thread(target=FB().fabiao, args=("918测试标-02", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t11 = threading.Thread(target=touzi().PC_touzi, args=("13876767676", "a12345678", "专业测试一次性还款", "2008", "a1234567", "null"))
t12 = threading.Thread(target=touzi().PC_touzi, args=("15821903152", "a1234567", "专业测试一次性还款", "1007", "Chq199312", "null"))




# t1.start()




if __name__ == '__main__':
    DL =FB()
    t500 = threading.Thread(target=DL.fabiao, args=("chq专用标", "chq专用红包方案", "chq专用加息券方案", "AC20171106150947", "1000000", "10", "60", "0.5"))
    t500.start()


# t300.start()
# t301.start()
# t302.start()
# t303.start()
# t304.start()




# t60.start()
# time.sleep(1)
# t70.start()
# time.sleep(1)
# t80.start()
# time.sleep(1)
# t90.start()
# time.sleep(1)
# t100.start()








#t7.start()
#t8.start()
#t9.start()
#10.start()


#t4.start()
#time.sleep(2)
#t5.start()



#t10.start()
#time.sleep(25)

#t12.start()
#t11.start()





"""
t1 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-04", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t2 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-05", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t3 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-06", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t4 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-07", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t5 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-08", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t6 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-09", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t7 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-10", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t8 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-11", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t9 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-12", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t10 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-13", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))
t11 = threading.Thread(target=FB().fabiao, args=("10天派息测试标-14", "chq大转盘红包方案", "邀请好友方案", "chq大额返现", "1000000", "10", "30", "0.5"))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
#t6.start()
#t7.start()
#t8.start()
#t9.start()
#t10.start()
#t11.start()
"""







