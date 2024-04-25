# !/user/bin/env python3
# -*- coding: utf-8 -*-
import pyautogui
import time
# 查看电脑屏幕点大小
# width,height=pyautogui.size()
# print(f'您的电脑像素为:{width}x{height}')
# pyautogui.moveTo将鼠标立即移动到指定位置，可传三个参数，
# for i in range(5):
#     pyautogui.moveTo(100,100,duration=0.25)
#     pyautogui.moveTo(200,100,duration=0.25)
#     pyautogui.moveTo(200,200,duration=0.25)
#     pyautogui.moveTo(100,200,duration=0.25)

# pyautogui.moveRel鼠标相对当前位置进行移动，参数个数同上，第一第二个参数是相对往右往下移动，调为负数则是向左向上移动
# for i in range(5):
#     pyautogui.moveRel(100,0,duration=0.1)
#     pyautogui.moveRel(0,100,duration=0.1)
#     pyautogui.moveRel(-100,0,duration=0.1)
#     pyautogui.moveRel(0,-100,duration=0.1)

# 调用鼠标当前位置
time.sleep(3)
print(pyautogui.position())

# pyautogui.click鼠标点击事件，前两个参数指定位置，第三个参数button可指定鼠标的按钮,left,right,middle
# pyautogui.mouseDown，只是按下鼠标按钮
# pyautogui.mouseUp，只是释放鼠标按钮
# pyautogui.doubleClick，执行双击鼠标左键
# pyautogui.rightClick，双击鼠标右键
# pyautogui.middleClick，双击鼠标中键
# pyautogui.click(1000,900,button='right')

# pyautogui.dragRel相对当前位置往某个方向拖动，按住某个按钮拖到
# time.sleep(5)
# pyautogui.click()
# distance=200
# while distance>0:
#     pyautogui.dragRel(distance,0,duration=0.1,button='left')#向右移动
#     distance=distance-5
#     pyautogui.dragRel(0,distance,duration=0.1,button='left')#向下移动
#     pyautogui.dragRel(-distance,0,duration=0.1,button='left')#向左移动
#     distance=distance-5
#     pyautogui.dragRel(0,-distance,duration=0.1,button='left')#向上移动

# pyautogui.scroll()鼠标滚动，正值向上，负值向下
# time.sleep(6)
# pyautogui.scroll(-300)

# pyautogui.screenshot()该函数会返回一个屏幕快照的image对象
# im=pyautogui.screenshot()
# im.save('./123.png')

# image对象getpixel()传入坐标元组告诉你这些坐标处的像素颜色
# print(im.getpixel((23,56)))

# pyautogui.pixelMatchesColor()第一个第二个参数是x,y坐标，第三个参数是是一个元组，包含三个参数，如果颜色匹配，返回true
# print(im.getpixel((500,200)))
# result=pyautogui.pixelMatchesColor(500,200,(233, 230, 232))
# print(result)

# 微信点击发送的事件
import cv2

# 获取带有微信的屏幕快照并且保存到本地
# im=pyautogui.screenshot()
# im.save('./weixin.png')
#
# # 基于cv2读取照片
# screen=cv2.imread('./weixin.png')
# submit=cv2.imread('./submit.png')
# # .shape获取图片的像素,是高x宽
# print(screen.shape,submit.shape)

# 在屏幕快照中对比发送按钮，定位其准确位置
# result=cv2.matchTemplate(submit,screen,cv2.TM_CCOEFF_NORMED)
# # print(result)
# # result是一个二维列表，列表中最大元素的位置就是我们对比后相似度最高的图片
#
# # minManLoc返回一个元组，其中四个元素，为最不相似点数，最相似点数，以及他们两个的坐标
# pos_start=cv2.minMaxLoc(result)[3]#获取最相似点的坐标
# print(pos_start)#返回的是图片左上角的坐标

# 定位到点击图片的中间位置
# x=int(pos_start[0]+int(submit.shape[1]/2))
# y=int(pos_start[1]+int(submit.shape[0]/2))
#
# time.sleep(5)
# pyautogui.click(x,y)



