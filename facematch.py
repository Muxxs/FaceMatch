# coding=utf-8
import itchat, os

import os.path

shatdown=0
filehelper="@4383b58035f4bfb2b2a2cdd1d46c349e52919e71d1b6a7cdd3c9a6ca6718cd2a"
yesorno="1"    #1为一人一票，0为疯狂投票
import time

text = open('列表.txt', 'r')
print(text)
def panduan(text):
    if yesorno=="0":
        return 0
    else:
        user=open('user.txt','r')
        user=user.read()
        if not user.find(text)==-1:
            return -1
        else:
            return 0


def info(text,user):
    if not str(text.find("列表")) == "-1":
        return liebiao()
    if not str(text.find("投票")) == "-1":
        if panduan(user)==-1:
            return "现在是一人一票模式，不得多次投票"
        else:
            return toupiao(text[3:],user)
    if not str(text.find("总排名")) == "-1":
        return paiming("")
    return ""


def liebiao():  #返回列表
    text = open('列表.txt', 'r')
    text = text.read()
    tex = text.split("\n")
    lib = ""
    for i in tex:
        i = i.split("=")
        if lib == "":
            lib = i[0]
        else:
            lib = lib + "、" + i[0]
    print(lib)
    return lib


def toupiao(name,user): #返回投票📖
    lines = open('列表.txt').readlines()
    lib = ""
    for ij in lines:
        i = ij.split("=")
        print(ij)
        if not i == "" or not ij == "finish":
            if i[0] == name:
                i[1] = str(int(i[1]) + 1)
                last = i[1]
        lib = lib + i[0] + "=" + i[1] + "\n"
    lib = lib + "finish"
    lib.replace("\n\n", "\n")
    libs = lib.split("\n")
    fp = open('列表.txt', 'w')
    for s in libs:
        print(s)
        if not s == "":
            if s == "finish":
                fp.close()  # 关闭文件
            else:
                fp.write(str(s) + "\n")
    try:
        print(name + "目前共有：" + str(last) + "票")
        fp = open('user.txt', 'w')
        fp.write(user+"  To  "+name+"\n")
        return name + "目前共有：" + str(last) + "票"
    except:
        return "没有"+name+"选手"


def paiming(user):
    if not user=="":
        os.system(user)
    lines = open('列表.txt').readlines()
    player = []
    for ij in lines:
        i = ij.split("=")
        if not i == "" or not ij == "finish":
            i[1] = i[1].replace("\n", "")
            player.append((i[0], int(i[1])))
    player = sorted(player, key=lambda student: student[1], reverse=True)
    alla = ""
    m = 0
    for i in player:
        m = m + 1
        alla = alla + "第" + str(m) + '名：选手"' + i[0] + '"的票数为' + str(i[1]) + "票\n"
    print(alla)
    return alla

def miaoshu(user):
    text = open("text/"+user+'.txt', 'r')
    text = text.read()
    if not text=="":
        lines=text
        if  lines.find("<>|")==-1:
            fp = open("text/" + user + '.txt', 'w')
            fp.write(lines + "<>|1")
            fp.close()
            return lines+"\n您是第一个看他的人！"
        else:
            print(lines)
            lines = lines.split("<>|")
            lines[1] = str(int(lines[1]) + 1)
            fp = open("text/" + user + '.txt', 'w')
            fp.write(lines[0] + "<>|" + lines[1])
            fp.close()
            print(lines)
            return lines[0]+"\nTa已经被看了"+str(lines[1])+"次"
    else:
        return

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    import shutil
    if not msg['Text'][:3].find("参选")==-1:
        return canxuan(msg['Text'][3:])
    print(msg["Text"])
    live=dieorlive()
    print(live)
    if live==1:
        return ""
    if not msg['Text'].find("7654312")==-1:
        paiming(msg['Text'][8:])
    if not msg['Text'].find('123001116')==-1:
        admin(msg['Text'][10:])
    print(msg['Text'])
    print(msg['FromUserName'])
    if msg['FromUserName'] == filehelper:
        msg['FromUserName'] = "filehelper"
    ret = info(msg["Text"],msg['FromUserName'])
    if ret=="":
        try:
            shutil.copyfile("pic/"+msg['Text']+".jpg", "t.png")
            itchat.send('@img@%s' % 't.png', toUserName=str(msg['FromUserName']))
            os.remove("t.png")
            return miaoshu(msg['Text'])
        except:
            pass
    return ret
def dieorlive():
    fp = open("sys/shat.txt", 'r')
    text=fp.read()
    fp.close()
    if text=="1":
        print("1")
        return 1
    else:
        return 0
def shadown():
    fp = open("sys/shat.txt", 'w')
    fp.write("1")
    fp.close()
def Restart():
    os.remove("sys/shat.txt")
def admin(order):
    if order=="Clean":
        os.remove("user.txt")
    if order=="Shat Down":
        shadown()
    if order=="Restart":
        Restart()
    if not order.find("投票")==-1:
        num=10
        for i in range(0,num):
            toupiao(order[3:],"")
def canxuan(text):
    import shutil
    text=text.split(" ")
    name=text[0]
    photo=text[1]
    infor=text[2]
    print("name:"+name+"\nurl:"+photo+"\ntext:"+infor)
    lines = open('列表.txt').readlines()
    lib = ""
    for ij in lines:
        i = ij.split("=")
        print(ij)
        lib = lib + i[0] + "=" + i[1] + "\n"
    lib.replace("\n\n", "\n")
    libs = lib.split("\n")
    fp = open('列表.txt', 'w')
    for s in libs:
        print(s)
        if not s == "":
            fp.write(str(s) + "\n")
    fp.write(name+"="+"0\n")
    fp.close()
    fp = open("text/"+name+'.txt', 'w')
    fp.write(infor)
    fp.close()
    os.system("wget "+photo)
    photo_name=photo.split("/")[-1]
    shutil.copyfile(photo_name,"pic/" + name + ".jpg")
    ret=miaoshu(name)
    print(ret)
    return ret
itchat.auto_login(hotReload=True)


itchat.run()
