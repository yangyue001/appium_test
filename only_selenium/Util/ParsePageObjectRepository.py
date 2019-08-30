from configparser import ConfigParser
import os


project_path = os.path.dirname(os.path.dirname(__file__))# 项目绝对路径

page_object_path = project_path+'/Conf/PageObjectRepository.ini'#配置文件绝对路径
class parsepageobjectrepository():
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_path)

    def getItemSection(self,section_name):
        #print(self.cf.items(section_name))
        return dict(self.cf.items(section_name))
    def getOptionValue(self,sectionName,optionName):#返回一个字典
        #print(self.cf.get(sectionName,optionName))
        return self.cf.get(sectionName,optionName)

if __name__ == '__main__':
    pp = parsepageobjectrepository()
    pp.getItemSection("smart_buy")
    pp.getOptionValue('smart_buy','buy_smartbid.smart_amount')