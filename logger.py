#!/usr/bin/python

import subprocess, sys, json

# чтение файла настроек и конфигурация
conf=json.load(open(logger_conf.json))
path=conf["Logs_path"]
files=conf["Logs_files"]

grep_list = ["grep"]

if False:  # добавить валидацию аргументов
#if sys.argv.count("*") == 1:
    print("Error")  # инструкция какие аргументы вводить
else:
    for param in sys.argv[1:]:
        grep_list.append(param)
    output=subprocess.check_output(grep_list)
    output=str(output)
    print(output)

