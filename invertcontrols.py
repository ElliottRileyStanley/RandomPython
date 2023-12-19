import pyautogui
import random
import time
pyautogui.PAUSE = 0
previous = [int(pyautogui.position()[0]), int(pyautogui.position()[1])]
invert = True
while True:
    if invert:
        current = [int(pyautogui.position()[0]), int(pyautogui.position()[1])]
        pyautogui.moveTo(int(previous[0]-(current[0]-previous[0])), int(previous[1]-(current[1]-previous[1])))
        previous = [int(previous[0]-(current[0]-previous[0])), int(previous[1]-(current[1]-previous[1]))]
        
    else:
        time.sleep(0.01)
        if random.randrange(1, 500) == 250:
            invert = True
            print("Invert")
            previous = [int(pyautogui.position()[0]), int(pyautogui.position()[1])]