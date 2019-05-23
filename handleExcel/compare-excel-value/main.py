"""
# 对比两张 excel 表的内容数值不同
# 假设两张表结构一致
# 不存在合并单元格
"""

import os
import xlrd
import xlwt
import time

# 读取文件并比对
def read_excel(ori_path,tar_path,sub_name):
        success = 0 
        fail = 0
        origin_xls = {}
        target_xls = {}

        wb_ori = xlrd.open_workbook(ori_path)
        wb_tar = xlrd.open_workbook(tar_path)

        sheet_num = len(wb_ori.sheets())  #记录子表数量

        startime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #获取系统时间
        print(startime,"开始比对...")

        logname = "log_" + startime[0:10] + '.log'
        logfile = open(logname,'w')  #创建文件，如果已存在则被覆盖
        logfile.writelines(startime+':【开始比对】...'+'\n')
        logfile.close()

        try:
                sheet_ori = wb_ori.sheet_by_name(sub_name)
                sheet_tar = wb_tar.sheet_by_name(sub_name)
                if sheet_tar.name == sheet_ori.name:  #如果表名相同
                        if sheet_ori.name == sub_name:
                                #将数据存入 dictionary
                                for rows in range(1,sheet_ori.nrows):
                                        ori_list = sheet_ori.row_values(rows)  #源表每一行的值(数组)
                                        tar_list = sheet_tar.row_values(rows)
                                        origin_xls[rows] = ori_list
                                        target_xls[rows] = tar_list
                                if origin_xls[1] == target_xls[1]:
                                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 表头一致')
                                
                                for ori_num in origin_xls:
                                        flag = 'false'  #判断是否一致
                                        for tar_num in target_xls:
                                                if origin_xls[ori_num] == target_xls[tar_num]:
                                                        print(origin_xls[ori_num])
                                                        print(target_xls[tar_num])
                                                        flag = 'true'
                                                        break
                                        if flag=='true':  #匹配上结果输出后台日志
                                                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' row:%d is ok'%ori_num)
                                                success+=1
                                        else:  #匹配不上将源表中行记录写入txt
                                                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' row:%d is different'%ori_num)
                                                fail+=1
                                                data=origin_xls[ori_num]
                                                logstr='【不一致】row<'+str(ori_num)+'>:'+str(data)
                                                logfile_append(logname,logstr)
                else:
                        errmsg='【'+sub_name+'】子表名不一致'
                        logfile_append(logname,errmsg)
        except Exception as err:
                logfile_append(logname,str(err)) #输出异常


#增加 log 文件
def logfile_append(filename,content):
        file = open(filename,'a')  #以追加方式打开文件夹
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #系统时间格式化
        file.writelines(time_now+':'+content+'\n')  #写入内容
        file.close()

def main():
        pass

if __name__ == '__main__':
        read_excel('original.xlsx','target.xlsx','test')