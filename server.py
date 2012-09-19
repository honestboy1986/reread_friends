#coding:utf-8
from bottle import route, run, mako_view, request, response,redirect
from service import insert_user, insert_weibo
from models import User, Feed
from store import get_db
import re
import datetime 
@route("/reg")
@mako_view("template/reg.html")
def reg():
    return dict()

@route("/reg_action", method="POST")
@mako_view("template/reg.html")
def reg_action():
    db = get_db()
    email = request.forms["email"]
    name = request.forms["name"]
    w = db.session.query(User).filter(User.email==email)
    if w.count()>0:
        return dict(err="邮箱已被占用")
    p = re.compile("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")
    email_style =  p.match(request.forms["email"])
    if email_style:
        if request.forms["password"] == request.forms["re_password"]: 
            insert_user(request.forms["email"], request.forms["name"], request.forms["password"])
            response.set_cookie("email",email,secret="123456")
            response.set_cookie("name",name,secret="123456")
            redirect("/xiongdihui") 
        else: 
            return dict(err="密码错误")
    else:
        return dict(err="email格式错误")

@route("/")
@mako_view("template/login.html")
def login():
    email = request.get_cookie("email",secret="123456")
    if email:
        redirect("/xiongdihui")
    else:
        return dict()
@route("/exit")
def exit():
    response.set_cookie("email",None,secret="123456")
    redirect("/")

@route("/login_action", method="POST")
@mako_view("template/login.html")
def login():
    db = get_db()
    email = request.forms["email"]
    password = request.forms["password"]
    r = db.session.query(User).filter(User.email==email,User.password==password)
    if r.count()>0:
        print r[0]
        response.set_cookie("name", r[0].name, secret="123456")
        response.set_cookie("email",email,secret="123456")
        redirect("/xiongdihui")
    else:
        return dict(err="用户名或密码错误！")
@route("/xiongdihui")
@mako_view("template/xiongdihui.html")
def xiongdihui():
    db = get_db()
    email = request.get_cookie("email",secret="123456")
    name = request.get_cookie("name",secret="123456")
    feeds = db.session.query(Feed).filter(Feed.email==email)
    return dict(weibo_action=feeds, name=name)
@route("/weibo_action", method="POST")
@mako_view("template/xiongdihui.html")
def weibo():
    content = request.forms["weibo"]
    f_time = datetime.datetime.now()
    email = request.get_cookie("email",secret="123456")
    insert_weibo(email, content, f_time)
    redirect("/xiongdihui")
@route("/fans")
@mako_view("template/fans.html")
def get_fans():
    db = get_db()
    fans = db.session.query(User).filter() 
    f_content = db.session.query(Feed).filter()
    return dict(users=fans,f_content=f_content)   
@route("/information")
@mako_view("template/information.html")
def information():
    db = get_db()
    email = request.get_cookie("email",secret="123456")
    n = db.session.query(User).filter(User.email==email)
    return dict(email=email,n=n)
@route("/change_information")
def change_information():
    user = User()
    user.phonenumber = request.forms["phonenumber"]
    user.address = request.forms["address"]
    session.save(user)
    
run(host="192.168.0.9", port="8080")
