#coding:utf-8
from sys import argv, exit
import os
script, tongxunlu = argv
f = open(tongxunlu, 'w+')
name = []
tele = []
qqnum = []
            
def add_friends():
    new_friends = raw_input("请输入新的联系人：")
    if new_friends in name:
        print "该用户名已被占用！"
        start()
    name.append(new_friends)
    long = int(len(name))
    new_telephone = raw_input("请输入电话号码：")
    tele.append(new_telephone)
    qqnumber = raw_input("请输入qq号码：")
    qqnum.append(qqnumber)
    save_friends()
    print "添加用户成功！"
    start()
        
def edit_friends():
    edit = raw_input("输入用户名：")
    if edit in name:
        a = raw_input("是否更改用户名:(Y/N)")
        for i in (add_friends.long-1):
            if a == "y":
                if name[i] == edit: 
                    position = i                
                    change_name(i)
                else:
                    print "name err"
            else:
                continue
            t = raw_input("是否更改用户电话:(Y/N)")
            if t == "y":
                change_tele(i)
            else:
                continue
            q = raw_input("是否更改用户qq：(Y/N)")
            if q == "y":
                change_qqnum(i)
            else:
                start()
    else:
        print "此用户不存在！"
def change_name(i):
    name[i] = raw_input("输入新的用户名：")
    f.write(str(name))
def change_tele(j):
    new_t = raw_input("输入新的用户电话：")
    re_tele = raw_input("重新输入新的用户电话：")
    if new_t == re_tele:
        tele[j] = re_tele
def change_qqnum(a):
    old_qq = raw_input("输入旧的qq号码：")
    if qqnum[a] == old_qq:
        qqnum[a] = raw_input("输入新的qq号码：")
        f.write(str(qqnum))        
        
def find_friends():
    find = raw_input("请输入用户名,密码，或qq：")
    for i in range(add_friends.long-1):
        if name[i] == find:
            print name[i], tele[i], qqnum[i]
        elif tele[i] == find:
            print name[i], tele[i], qqnum[i]
        elif qqnum[i] == find:
               print name[i], tele[i], qqnum[i]
        else:
               print "输入信息有误！"        
    
def remove_friends():
    re = raw_input("请输入要删除的用户名：")
    for i in (add_friends.long-1):
        if name[i] == re:
            remove(name[i])
            remove(tele[i])
            remove(qqnum[i])
            save_friends():
        else:
            print "输入的用户名不存在！"
            
def save_friends():
    f.write(str(name))
    f.write(str(tele))
    f.write(str(qqnum))
def all_friends():
    f.readlines()
f.close()
print """
+******************操作菜单****************+
|查看所有联系人(all) | 查找联系人    (find)|
|添加联系人    (add) | 删除联系人  (remove)|
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
    elif a == "find":
        find_friends()
    elif a == "remove":
        remove_friends()
    elif a == "save":
        save_friends()
    elif a == "quit":
        exit(0)
    else:
        print "输入命令错误！请重新输入，如需帮助请输入help！"


start()
