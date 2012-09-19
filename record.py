#-*-coding:utf-8 -*-
from sys import argv, exit
import os
script, tongxunlu = argv
f = open(tongxunlu, 'r')
arr = f.read().split("\n")
name = []
tele = []
qqnum = []
if len(arr) == 3:
    name = eval(arr[0])
    tele = eval(arr[1])
    qqnum = eval(arr[2])
def add_friends():
    new_friends = raw_input("请输入新的联系人：")
    if new_friends in name:
        print "该用户名已被占用！"
        add_friends()
    name.append(new_friends)
    new_telephone = raw_input("请输入电话号码：")
    tele.append(new_telephone)
    qqnumber = raw_input("请输入qq号码：")
    qqnum.append(qqnumber)
    start()    
def edit_friends():
    edit = raw_input("输入要编辑的用户名：")
    if edit in name:
        for i in range(0,int(len(name))):
            if name[i] == edit: 
                r = i            
                change_name(r)
    else:
        print "此用户不存在！"
        edit_friends()
def change_name(r):
    n = raw_input("是否修改此用户名:(Y/N)")
    if n == "y":
        name[r] = raw_input("输入新的用户名：")
        print "修改到文件！！！！！！！！！！！save_name()"
        change_tele(r)
    elif n =="n":
        change_tele(r)
    else:
        print "输入错误！！！请从新输入"
        change_name(r)
def change_tele(r):
    t = raw_input("是否更改用户电话:(Y/N)")
    if t == "y":
        new_t = raw_input("输入新的用户电话：")
        re_tele = raw_input("重新输入新的用户电话：")
        if new_t == re_tele:
            tele[r] = re_tele
            print "修改成功 。。。。。。。。"
            change_qqnum(r)
        else:
            print "两次输入不同！"
            change_tele()   
    elif t =="n":
        change_qqnum(r)
    else:
        print "输入错误 请从新输入！！"
        change_tele(r)
def change_qqnum(r):
    q = raw_input("是否更改用户qq：(Y/N)")
    if q == "y":
        new_qq = raw_input("输入新的qq号码：")
        qqnum[r] = new_qq
        print "修改到文件 新的qq号码为 %s" % qqnum[r]
        start()
    elif q == "n":
        start()
    else:
        print "输入错误 请从新输入！！"
        change_qqnum(r)       
        
def find_friends():
    find = raw_input("请输入用户名,密码，或qq：")
    if find in name or find in tele or find in qqnum:
        for i in range(0,int(len(name))):
            if name[i] == find or tele[i] == find or qqnum[i] == find:
                print "name is %s\nand telephone is %s,\nand qqnumber is %s" % (name[i], tele[i], qqnum[i])
                start()   
    else:
        print "输入信息有误！"
        start()        
    
def remove_friends():
    re = raw_input("请输入要删除的用户名：")
    if re in name:
        for i in range(0,int(len(name))):
            if name[i] == re:
                name.remove(name[i])
                tele.remove(tele[i])
                qqnum.remove(qqnum[i])
                print "删除%s的所有信息！,请保存修改。" % re
                start()
    else:
        print "输入的用户名不存在！"  
        start()
def save_friends(name,tele,qqnum):
    f = open(tongxunlu,"w")
    f.write(str(name))
    f.write("\n")
    f.write(str(tele))
    f.write("\n")
    f.write(str(qqnum))
    f.close()
    print "信息已保存！"
    f.close()
    start()
def all_friends():
    print "print all name here!"
    f = open(tongxunlu,"r")
    n = f.read().split("\n")
    print n[0]
    a = raw_input("查看所有信息！！（Y/N）")
    if a == "y":
        print n[0]
        print n[1]
        print n[2]
        f.close()
        start()
    else:
        print "继续操作...！"
        f.close()
        start()

print """
+******************操作菜单****************+
|查看所有联系人 (all)| 查找联系人    (find)|
|添加联系人     (add)| 删除联系人  (remove)|
|编辑联系人    (edit)| 保存并退出    (save)|
|使用帮助      (help)| 退出但不保存  (quit)| 
+------------------------------------------+
"""
def start():
    a = raw_input("请输入菜单命令：")
    if a == "all":
        all_friends()
    elif a == "add":
        add_friends()
    elif a == "edit":
        edit_friends()
    elif a == "help":
        print "输入菜单中的命令即可操作文件!"
        start()
    elif a == "find":
        find_friends()
    elif a == "remove":
        remove_friends()
    elif a == "save":
        save_friends(name, tele, qqnum)
    elif a == "quit":
        exit(0)
    else:
        print "输入命令错误！请重新输入，如需帮助请输入help！"
        start()
start()
