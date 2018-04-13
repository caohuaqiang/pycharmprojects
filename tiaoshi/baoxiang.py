import unittest
import requests
from pprint import pprint
from diaoyong import readini
from diaoyong.denglu import denglu



class baoxiang(unittest.TestCase, denglu):
    """开宝箱活动"""
    def setUp(self):
        self.yuming = 'https://www-t.jfcaifu.com'
        print('test start!!!')

    def tearDown(self):
        print('test over!!!')

    def test_wap(self):
        session = requests.session()
        url_dl = self.yuming + '/wap/user/doLogin.html'                                                         #登录接口
        data_dl = self.denglu_wap(name='test')
        # pprint(data_dl)
        # print(type(data_dl))
        response_dl = session.request(method='post', url=url_dl, params=data_dl)
        json_dl = response_dl.json()
        if response_dl.status_code == 200 and json_dl['msg'] == '登录成功！':

            # pprint(json_dl)
            dl_cookies = response_dl.cookies
        else:
            raise Exception('登录接口请求失败，非200')
#---------------------------------------------------------------------------------------------------------------------------------
        url_luckyBoxList = self.yuming + '/luckybox/luckyBoxList.html'                                          #查看宝箱记录接口
        data_luckBoxList = {'userId': dl_cookies['userId']}
        print('查看宝箱记录接口，传参为： ', data_luckBoxList)

        response_luckyBoxList = session.request(method='get', url=url_luckyBoxList, params=data_luckBoxList)

        json_luckyBoxList = response_luckyBoxList.json()
        print('查看宝箱记录接口请求返回json如下：')
        pprint(json_luckyBoxList)


        if json_luckyBoxList['result'] :
            box = json_luckyBoxList['box']
            print('-----------------------box字典如下----------------------------')
            pprint(box)
        else:
            print('尚未有任何开宝箱记录')


# #----------------------------------------------------------------------------------------------------------
        url_prize = self.yuming + '/receive/prize.html'                                                       # 领取宝箱接口
        data_prize = {'userId': dl_cookies['userId'],
                      'boxs': "box_1"}
        response_prize = session.request(method='post', url=url_prize, params=data_prize)
        if response_prize.status_code == 200:
            json_prize = response_prize.json()
            print('=========================领奖接口返回json如下=============================')
            pprint(json_prize)

        else:
            raise Exception('领奖失败')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(baoxiang('test_wap'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

