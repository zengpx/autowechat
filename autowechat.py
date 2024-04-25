# !/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import os
import pyautogui
import time

import pyperclip

time.sleep(2)

#从屏幕screen中找到source的位置坐标(找到微信搜索框的位置)
def fingimg():
    im=pyautogui.screenshot()
    im.save('screen.png')
    screen=cv2.imread('./screen.png')
    sousuo=cv2.imread('./wechat.png')
    result=cv2.matchTemplate(sousuo,screen,cv2.TM_CCOEFF_NORMED)
    pot_start=cv2.minMaxLoc(result)[3]
    x=int(pot_start[0]+int(sousuo.shape[1])/2)
    y=int(pot_start[1]+int(sousuo.shape[0])/2)
    return x,y

#向搜索框录入要查找的好友名称,x,y为搜索框位置
def send_name_to_search(x,y,name):
    pyautogui.click(x,y)
    time.sleep(1)
    #赋值好友名称
    pyperclip.copy(name)
    #粘贴复制内容
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('enter')

#向好友发送消息
def send_msg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.hotkey('enter')

x,y=fingimg()
send_name_to_search(x,y,'文件传输助手')
time.sleep(2)
send_msg('i love python')

x,y=fingimg()
send_name_to_search(x,y,'李伟豪')
time.sleep(2)
send_msg('i love python')
# 你好

