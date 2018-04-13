import time
import hashlib
import base64
from diaoyong.readini import INI

class denglu():
    def denglu_ios(self) -> dict:
        """
        返回data字典：
        data = {'appkey': ***,
                'signa': ***,
                 'ts': ***,
                 'id': ***,
                 'pwd': ***}
        其中，id 和 pwd 取自ini文件夹下的配置文件config.ini的[user]区域的username、password
        """

# 加密规则：
# 1.appkey = 'V/SQ/yTyYjDmNLXB2unELw==' (死值)
# 2.给定一个固定字符串 a = 'LzgvD74cyEspGADEKOxAhA=='
# 3.ts 为当前时间的时间戳（中国上海） 10位数字
# 4.signa 加密方式为 md5加密  16位小写
# 5.pwd 密码  加密方式为  base64加密
#
# 以下为signa加密方式：
# 1.获取到 当前时间的时间戳ts
# 2.将给定的固定字符串a与ts拼接得到一个新的字符串，并进行md5加密
# 3.将上一步得到的字符串与appkey拼接，得到一个新的字符串，进行md5加密
# 4.最后将得到的字符串转为大写，获得到的新字符串即为signa


        appkey = 'V/SQ/yTyYjDmNLXB2unELw=='                     #固定值，得到了appkey
        a = 'LzgvD74cyEspGADEKOxAhA=='

        ts = int(time.time())
        print('ts: ', ts)

        A = a + str(ts)
        A_md5 = hashlib.md5(A.encode('utf-8'))
        B = A_md5.hexdigest() # 按16位输出


        C = B + appkey
        C_md5 = hashlib.md5(C.encode('utf-8'))
        D = C_md5.hexdigest() # 按16位输出

        signa = D.upper()                                       #转成大写，得到了signa
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


        return data




    def denglu_wap(self, name) -> dict:
        """wap登录，返回一个字典"""
        filepath = '../ini/user.ini'
        user = eval(INI().ini(filepath).get('user', name))
        mobilephone = user['username']
        pwd = user['password']
        return {'mobilePhone': mobilephone,
                'pwd': pwd}



