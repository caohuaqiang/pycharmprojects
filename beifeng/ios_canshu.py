import time
import hashlib
import base64
import requests
from diaoyong.readini import INI
import pprint


"""
加密规则：
1.appkey = 'V/SQ/yTyYjDmNLXB2unELw==' (死值)
2.给定一个固定字符串 a = 'LzgvD74cyEspGADEKOxAhA=='
3.ts 为当前时间的时间戳（中国上海） 10位数字
4.signa 加密方式为 md5加密  16位小写
5.pwd 密码  加密方式为  base64加密   

以下为signa加密方式：
1.获取到 当前时间的时间戳ts
2.将给定的固定字符串a与ts拼接得到一个新的字符串，并进行md5加密
3.将上一步得到的字符串与appkey拼接，得到一个新的字符串，进行md5加密
4.最后将得到的字符串转为大写，获得到的新字符串即为signa
"""


appkey = 'V/SQ/yTyYjDmNLXB2unELw=='                     #固定值，得到了appkey
id = '15821903152'
pwd1 = 'YTEyMzQ1Njc='               #base64加密
a = 'LzgvD74cyEspGADEKOxAhA=='

ts = int(time.time())
print('ts: ', ts)

A = a + str(ts)
A_md5 = hashlib.md5(A.encode('utf-8'))
B = A_md5.hexdigest() # 按16位输出


C = B + appkey
C_md5 = hashlib.md5(C.encode('utf-8'))
D = C_md5.hexdigest() # 按16位输出

signa = D.upper()                                       #得到了signa
print('signa: ', signa)


peizhiwenjian = INI()
filepath = '../ini/user.ini'
wj = peizhiwenjian.ini(filepath)
user = eval(wj.get(section='user', option='chq'))   #从配置文件中拿到字符串，再转成字典

phone = user['username']
password = user['password']
pwd = base64.b64encode(password.encode(encoding='utf-8'))



data = {'appkey': appkey,
        'signa': signa,
        'ts': ts,
        'id': phone,
        'pwd': pwd}


url = 'https://www-t.jfcaifu.com/app/user/doLogin.html'

if __name__ == '__main__':
    session = requests.session()
    response = session.request(method='post', params=data, url=url)
    if response.status_code == 200:
        pprint.pprint(response.json())
    else:
        raise Exception('我操！ 请求失败了！')

