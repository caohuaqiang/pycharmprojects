import configparser
import os
from  selenium import webdriver
import time
import json



class CHQ():
    def quzhi(self):
        file_path = os.path.abspath(os.path.join('./', 'user.ini'))
        config = configparser.ConfigParser()
        config.read(file_path)

        browser = config.get("broswer_name", "broswer")     #分别代表所在区域名 和变量名
        url = config.get("server", "server")
        return (browser, url)


    def papapa(self):
        defaultconfig = {'base_url': 'https://www.baidu.com',
                         'account': '15821903152',
                         'password': 'a1234567'}
        # config = json.load(defaultconfig)

if __name__ == '__main__':
    A = CHQ()
    B = A.papapa()
    C = {'base_url': 'https://www.baidu.com',
                         'account': '15821903152',
                         'password': 'a1234567'}
    print(C['base_url'])