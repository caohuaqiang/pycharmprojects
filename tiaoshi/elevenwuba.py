import requests
from pprint import pprint
from diaoyong.denglu import denglu
import pymysql
from diaoyong.pmq import UseDataBase


class ele58(denglu):
    def __init__(self, phone):
        self.yuming = 'https://www-t.jfcaifu.com'
        self.phone = phone
        # self.db_config = {'host': '139.196.133.170',
        #                   'user': 'jftestuser',
        #                   'password': 'quton8RFKLuZynOV48yzyePnKZKBGz',
        #                   'database': 'jftest-t',
        #                   }
        self.db_config = {'host': '139.196.133.170',
                          'user': 'jftestuser',
                          'passwd': 'quton8RFKLuZynOV48yzyePnKZKBGz',
                          'database': 'jftest-t',
                          'cursorclass': pymysql.cursors.DictCursor}

    def test_login(self):
        path_login = '/activity/flying.html'
        path_code = '/wap/user/getActivityCode.html'
        session = requests.session()
        response_code = session.request(method='post', params={'mobilePhone': self.phone}, url=self.yuming + path_code)
        if response_code.status_code == 200:
            print('获取验证码接口:', end=' ')
            pprint(response_code.json())
        else:
            print('验证码接口翻车！！！')

        data_login = {'channelCode': '40409',
                      'pwd': 'a1234567',
                      'mobilePhone': self.phone,
                      'code': '888888'}
        response_login = session.request(method='get',url=self.yuming + path_login, params=data_login)
        if response_login.status_code == 200:
            print('注册接口返回json：', end=' ')
            pprint(response_login.json())
            with UseDataBase(config=self.db_config) as cursor:
                _SQL = "select user_id, user_name, pwd, mobile_phone, channel_type from rd_user where mobile_phone = %s" % self.phone
                cursor.execute(_SQL)
                contents = cursor.fetchall()
                # print(contents)
                # for line in contents:
                #     for data in line:
                #         print(data, end='->')
                # print(contents)
                for data in contents:
                    pprint(data)

        else:
            raise Exception('注册不成功')


if __name__ == '__main__':
    phone = '17302139307'
    Login = ele58(phone)
    Login.test_login()


