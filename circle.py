import math
import pyautogui

value = 0

while value < 6.28:
    pyautogui.moveTo(math.cos(value)*400+1920, math.sin(value)*400+560, 0)
    if value == 0:
        pyautogui.mouseDown()
    value += 0.09
pyautogui.mouseUp()