#encoding=utf-8
from xlrd import open_workbook
from Util.ParsePageObjectRepository import *

class parseExcel:

    def __init__(self,xls_name,sheet_name):
        self.xls_name = xls_name
        self.sheet_name = sheet_name

    def get_xls(self):
        """
        get interface data from xls file
        :return:
        """
        cls = []
        # get xls file's path
        xlsPath = os.path.join(project_path, "TestData",  self.xls_name)  # 获取Excel文件位置即文件名
        # open xls file
        file = open_workbook(xlsPath)  # 打开Excel文件
        # get sheet by name
        sheet = file.sheet_by_name(self.sheet_name)  # 获取Excel中对应的sheet
        # get one sheet's rows
        nrows = sheet.nrows  # 获取sheet中行的数量
        for i in range(nrows):  # 从第一行开始执行 初始i=0
            if sheet.row_values(i)[0] != u'case_name':  # 绕过第一行第一例内容为case_name的
                cls.append(sheet.row_values(i))  # 列表每一个元素存储的为整行内容列表形式，直到存满整个sheet值
        return cls
