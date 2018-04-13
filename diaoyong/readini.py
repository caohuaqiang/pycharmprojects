import configparser
import os


class INI():
    def ini(self, filepath:str):
        """读取ini配置文件，传入参数为文件路径（字符串格式），返回config对象，可对该对象使用config.get(section,name)方法取得相应的参数"""
        config = configparser.ConfigParser()
        config.read(filepath)
        return config



# if __name__ == '__main__':
#     A = INI()
#     file_path = '../ini/user.ini'     #  .当前目录    ..上一级目录
#     B = A.ini(file_path)
#     C = eval(B.get('user', 'chq'))    #  分别代表所在区域名 和变量名   字符串转为字典
#     print(C['username'], C['password'])