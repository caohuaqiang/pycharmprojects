from selenium import webdriver
import time
# coding = utf-8

class FB:
    def __init__(self, config: dict):
        self.config = config
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get('https://erp-t.jfcaifu.com/admin/login.html')
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("valicode").clear()
        driver.find_element_by_id("valicode").send_keys("jfcf")
        driver.find_element_by_xpath("html/body/div[1]/div/form/ul/li[5]/input").click()
        time.sleep(5)

    def Fa_Biao(self):
        driver = self.driver
        self.login()

        chq = driver.find_elements_by_xpath('//*[@id="nav"]/div[3]/div[1]/div[1]')
        for x in chq:
            if x.text == '借贷管理':
                x.click()

        time.sleep(2)
        driver.find_element_by_partial_link_text(u'借款初审').click()
#===============================================================================================================================================
        iframe_jiekuanchushen = "/html/body/div/div[2]/div/div/div[2]/div[2]/div/iframe"
        driver.switch_to.frame(driver.find_element_by_xpath(iframe_jiekuanchushen))  # 跳转到借款初审页面的iframe框架内
        driver.find_element_by_id("a").click()  # 发标
        time.sleep(1)

        iframe_tankuang = "/html/body/div[3]/div[2]/iframe"
        driver.switch_to.frame(driver.find_element_by_xpath(iframe_tankuang))  # 跳转到弹框页面(ifram嵌套，从第一层跳到第二层)

#-----------------------------------发标表单------------------------------------------------------------------------------------------------------
        # driver.find_element_by_xpath("html/body/form/div[1]/div/div[3]/i").click()  # 活动标
        driver.find_element_by_xpath("/html/body/form/div/div/div[2]/i").click()  # 热销中

        activity_list = self.config['activity']
        activity = driver.find_elements_by_css_selector('.layui-unselect.layui-form-checkbox')
        for a in activity:
            if a.text.split('\n')[0] in activity_list:
                a.click()
        print('--------------------------------------------')

        if self.config['is_recommend'] == 1:
            driver.find_element_by_xpath('/html/body/form/div[1]/div/div[5]/span').click()
        driver.find_element_by_id("ads").send_keys(self.config['bm'])  # 标名
        driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div/input").send_keys(self.config['product_number'])  # 项目编号

        red_path = '//*[@lay-value="%s"]' % self.config['redpacket']
        coupon_path = '//*[@lay-value="%s"]' % self.config['coupon']
        driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div/div/input").click()  # 弹出红包方案下拉框
        time.sleep(0.5)
        driver.find_element_by_xpath(red_path).click()

        driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div/div/div/input").click()  # 弹出加息券方案下拉框
        time.sleep(0.5)
        driver.find_element_by_xpath(coupon_path).click()

        driver.find_element_by_id("account").send_keys(self.config['money'])  # 标的金额
        driver.find_element_by_id("apr").send_keys(self.config['apr'])  # 年利率
        driver.find_element_by_id("timeLimit").send_keys(self.config['timelimit'])  # 标的天数
        driver.find_element_by_id("putStartTime").click()  # 开标时间
        driver.find_element_by_xpath(".//*[@id='laydate_ok']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@placeholder='请选择客服']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@lay-value='kefu123']").click()  # 客服
        driver.find_element_by_xpath('//*[@placeholder="请选择借款人邮箱"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@lay-value='745133655@qq.com']").click()  # 借款人
        # driver.find_element_by_xpath("//*[@lay-filter='save']").click()  # 确定，创建标完成

        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    config = {'bm': 'chq',
              'product_number': 'CHQ888',
              'is_recommend': 0,
              'redpacket': 'chq专用红包方案',
              'coupon': 'chq专用加息券方案',
              'activity': ['参与大额返现', '变态活动'],
              'money': '500000',
              'apr': '10',
              'timelimit': '60',

              }
    fb = FB(config)
    fb.Fa_Biao()







