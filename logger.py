#!/usr/bin/python

import subprocess, sys, json, datetime
from parser import Parser

conf=json.load(open('logger_conf.json'))
path=conf["Logs_path"]
files=conf["Logs_files"]
ext=conf["Ext"]

grep_list = ["xzgrep"]
params = sys.argv

def find_file(flag):
    if flag == '-mp':
        return files[0]
    elif flag == '-m':
        return files[1]
    elif flag == '-e':
        return files[2]
    else:
        print('Error! Wrong file flag!')
#        sys.exit(0)

def find_date(date):
    if date == datetime.datetime.today().strftime("%Y%m%d"):
        return ''
    else:
        date = datetime.datetime.strptime(date, "%Y%m%d")
        one_day = datetime.timedelta(1)
        date = date + one_day
        date = date.strftime("%Y%m%d") 
        if date == datetime.datetime.today().strftime("%Y%m%d"):
            return date
        else:
            return date + '.' + ext

if len(params) < 4:
    print("Error! Count of params < 3.")
#    sys.exit(0)
elif len(params) == 4:
    params[2] = find_file(params[2])
    params[2] = path + params[2]
    params[3] = find_date(params[3])
    if params[3] == '':
        del(params[3])
    else:
        params[2] = params[2] + "-" + params[3]  
        del(params[3])
#    print(params)
    for param in params[1:]:
        grep_list.append(param)
#    print(grep_list)
    output=subprocess.check_output(grep_list)
    parser=Parser()
    output=parser.parser(output.decode("utf-8"))
    print(output)
else:
    pass
 
