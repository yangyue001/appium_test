import os
import codecs
import configparser

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取绝对路径的第一个目录 例如：～/Downloads/interfaceTest
prodir =os.getcwd()
configPath = os.path.join(prodir, "PageObjectRepository.ini")  # 获取config.ini 的地址


class ReadConfig:
    def __init__(self):

        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:      ## 判断是否为带BOM文件
            data = data[3:]                 # 如果带就跳过BOM
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

        '''

        with open(configPath)as fd:
            data = fd.read()
            print(type(data))
            # remove BOM
            if data[:3]== codecs.BOM_UTF8:
                data = data[3:]
                with open(configPath,"w") as file :
                    file.write(data)
        '''


    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value