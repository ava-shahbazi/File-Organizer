import os
import glob
from khayyam import JalaliDatetime,JalaliDate

files_list = glob.glob('*')

extention_set = set()

for each_file in files_list:
    try:   
        extention = each_file.split('.')[1]
        extention_set.add(extention)
    except:
        continue

def creat_folder():
    for exe in extention_set:
        if exe == 'py':
            continue
        try:
            today = JalaliDate.today().strftime('%A %d %B %Y')
            os.makedirs(today + '/' + exe + "_files")
        except:
            continue

def move_file():
    for each_file in files_list:
        try:
            today = JalaliDate.today().strftime('%A %d %B %Y') 
            extention = each_file.split('.')[1]
            os.rename(each_file,today + '/' + extention +'_files/'+each_file)
        except:
            continue


creat_folder()
move_file()