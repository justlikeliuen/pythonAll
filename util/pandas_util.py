# -*- coding: utf-8 -*-
# @Author: En Liu
# @Date: 18/6/21
# @Description: excel export 工具类
import datetime
import traceback

import pandas as pd


class PP:
    def __init__(self,appid,openid):
        self.appid = appid
        self.openid = openid

def value_list(obj):
    varList = []
    for name,value in vars(obj).items():
        varList.append(value)
    return varList

def form(oo_list):
    du_list = []
    for obj in oo_list:
        du_list.append(value_list(obj))
    return du_list

def form_column(obj):
    varList = []
    for name,value in vars(obj).items():
        varList.append(name)
    return varList


def writeObjListToExcel(obj_list,file_path=("./"+datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")+".xlsx"),sheet_name='Sheet'):
    """ 将传入的list写入excel文件
    :param obj_list 数据对象集合。确认为"对象"集合，不要是dict。将会根据对象反解对象属性名称
    """
    try:
        if len(obj_list) > 0:
            column = form_column(obj_list[0])
            df = pd.DataFrame(data=form(obj_list),columns=column)
            writer = pd.ExcelWriter(file_path)
            df.to_excel(excel_writer=writer, sheet_name=sheet_name)
            writer.save()
    except:
        traceback.print_exc()

if __name__ == '__main__':
    pp_list = []
    pp = PP(1,2)
    pp_list.append(PP(1,2))
    pp_list.append(PP(2,3))
    file_path = r'./output1.xlsx'
    writeObjListToExcel(pp_list)





