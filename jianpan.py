# !/user/bin/env python3
# -*- coding: utf-8 -*-
import pyautogui
import time
# time.sleep(6)
# pyautogui.click(961,768)
# time.sleep(2)
# pyautogui.typewrite()键盘录入的内容，可以是字符串，列表，interval是输入每个字符的事件间隔
# pyautogui.typewrite('Hello World!',interval=0.01)

# 自动发送信息
# time.sleep(6)
# pyautogui.click(961,768)
# time.sleep(2)
# pyautogui.typewrite('Hello world!',interval=0.01)
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(2)
# pyautogui.typewrite('Hello world!',interval=0.01)

# 键盘按下和释放按键
time.sleep(4)
pyautogui.keyDown('shift')#按键按下
pyautogui.press('4')
pyautogui.keyUp('shift')#按键松开

# 键盘热键,接受多个键字符参数，按顺序按下，再按相反顺序松开
pyautogui.hotkey('ctrl','c')