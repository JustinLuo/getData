#encoding:UTF-8

#!/usr/bin/python

import urllib.request
import re
import csv

def getData(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('GBK')
    return data

# 匹配数据基本函数，提取精炼
def base(pattern,data):
    pattern = re.compile(pattern)
    match = re.findall(pattern, data)
    if match:
        return match[0]
    else:
        return ''

# 客户姓名
def getName(data):
    pattern = "\<input name=\"cli_Name\" type=\"text\" value=\"(.*?)\"";
    return base(pattern, data)

# 联系手机
def getMobile(data):
    pattern = "\<input name=\"phone\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 联系座机
def getPhone(data):
    pattern = "\<input name=\"phone1\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 联系地址
def getAddress(data):
    pattern = "\<input name=\"address\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 产品名
def getProName(data):
    pattern = "\<input name=\"pro_Name\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 购买日期
def getBuyDate(data):
    pattern = "\<input name=\"buyDate\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 产品型号
def getProNo(data):
    pattern = "\<input name=\"pro_No\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 产品类型
def getProType(data):
    pattern = "\<input name=\"pro_Type\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 受理网点
def getUnitName(data):
    pattern = "\<input name=\"unit_name\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 受理日期
def getRecDate(data):
    pattern = "\<input name=\"rec_Date\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 回访人员
def getPName(data):
    pattern = "\<input name=\"pname\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)
# 备注
def getRemark(data):
    pattern = "\<input name=\"remark\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 安装单号
def getInstallId(data):
    pattern = "\<input name=\"installId\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 安装费用
def getIMoney(data):
    pattern = "\<input name=\"i_money\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 安装日期
def getInstallDate(data):
    pattern = "\<input name=\"installdate\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 技术人员
def getTecName(data):
    pattern = "\<input name=\"tecName\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 购买商场
def getBuyMall(data):
    pattern = "\<input name=\"buymall\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 发票号
def getInvNo(data):
    pattern = "\<input name=\"inv_No\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 条形码
def getBar(data):
    pattern = "\<input name=\"Bar\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 生产日期
def getBornDate(data):
    pattern = "\<input name=\"bornDate\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 收费情况
def getICharge(data):
    pattern = "\<input name=\"I_charge\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)

# 购买价格
def getPrice(data):
    pattern = "\<input name=\"price\" type=\"text\" value=\"(.*?)\""
    return base(pattern, data)


def writeData(data,sname):
    str1 = getName(data)+','+getMobile(data)+','+getPhone(data)+','+getAddress(data)+','+getProName(data)+','+getBuyDate(data)+','+getProNo(data)+','+getProType(data)+','
    str2 = getUnitName(data)+','+getRecDate(data)+','+getPName(data)+','+getInstallId(data)+','+getIMoney(data)+','+getInstallDate(data)+','+getTecName(data)+','
    str3 = getBuyMall(data)+','+getInvNo(data)+','+getBar(data)+','+getBornDate(data)+','+getICharge(data)+','+getPrice(data)+'\n'

    strs = str1 + str2 + str3

    with open(sname, "a") as out_file:
        out_file.write(strs)

#i = '66'
url = 'http://as.vanward.com/account/Installshow.aspx?id='

number = 1000000
sname = '1-1000000.csv'

#14087500

for i in list(range(1, 1000089)):

    if i == number:
        s1 = number-1000000
        sname = s1+'-'+number+'.csv'
        number += 1000000

    urls = url + str(i)

    data = getData(urls)

    if getName(data) != '':
        writeData(data, sname)
        print('\033[0;32;40m')
        print(str(i)+'---------------------------------------------[OK]')
        print('\033[0m')
    else:
        print('\033[0;31;40m')
        print(str(i)+"---------------------------------------------[No Data]")
        print('\033[0m')

#    str1 = getName(data)+','+getMobile(data)+','+getPhone(data)+','+getAddress(data)+','+getProName(data)+','+getBuyDate(data)+','+getProNo(data)+','+getProType(data)+','
 #   str2 = getUnitName(data)+','+getRecDate(data)+','+getPName(data)+','+getInstallId(data)+','+getIMoney(data)+','+getInstallDate(data)+','+getTecName(data)+','
  #  str3 = getBuyMall(data)+','+getInvNo(data)+','+getBar(data)+','+getBornDate(data)+','+getICharge(data)+','+getPrice(data)+'\n'

  #  strs = str1 + str2 + str3
  #  print(strs)

#    with open(sname, "a") as out_file:
#        out_file.write(strs)



out_file.close()


    #print(getdata(url))
