import pyautogui
import time

time.sleep(3)
im = pyautogui.screenshot()
print(pyautogui.position())
print(im.getpixel(pyautogui.position()))