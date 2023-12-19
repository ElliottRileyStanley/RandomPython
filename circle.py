import math
import pyautogui

pyautogui.PAUSE = 0.01

def attempt_one(centerx, centery, radius):
    value = 0
    while value < math.pi*2+0.00001:
        pyautogui.moveTo(math.cos(value)*radius+centerx, math.sin(value)*radius+centery, 0)
        if value == 0:
            pyautogui.mouseDown()
        value += math.pi*2/75
    pyautogui.mouseUp()

def attempt_two(centerx, centery, radius):
    pyautogui.moveTo(centerx+radius, centery)
    pyautogui.mouseDown()
    pyautogui.moveTo(centerx, centery+radius)
    pyautogui.moveTo(centerx-radius, centery)
    pyautogui.moveTo(centerx, centery-radius)
    pyautogui.moveTo(centerx+radius, centery)
    pyautogui.mouseUp()

attempt_one(1440, 557, 300)

#I'm working