import pyautogui
import numpy
import random
import time

strat = open(r'Primer\AI\newstrat.text').readlines()
heads = 1
tails = 0
flips = 67

def calibrate_mouse():
    input("Press enter when you are in position")
    return pyautogui.position()

def has_changed(startx, endx, starty, endy):
    for x in range(startx,endx):
        for y in range(starty,endy):
            if im_prev.convert('RGB').getpixel([x,y]) != im_new.convert('RGB').getpixel([x,y]):
                return True
    return False

def choiceaoeu(heads, tails, flips, strat):
    if heads + tails > 20 or flips == 0:
        return (random.randrange(1,2))
    else:
        return strat[int(((21*22/2)+1)*min(flips, 20)+((heads+tails)*(heads+tails+1)/2)+tails)][0]
    

heads1x, heads1y = calibrate_mouse()
heads2x, heads2y = calibrate_mouse()
tails1x, tails1y = calibrate_mouse()
tails2x, tails2y = calibrate_mouse()
score1x, score1y = calibrate_mouse()
score2x, score2y = calibrate_mouse()
flipx, flipy = calibrate_mouse()
fairx, fairy = calibrate_mouse()
cheatx, cheaty = calibrate_mouse()

while flips >=0:
    im_prev = pyautogui.screenshot()
    choice = choiceaoeu(heads, tails, flips, strat)
    print(choice)
    if int(choice) == 0:
        pyautogui.click(flipx, flipy)
    elif int(choice) == 1:
        pyautogui.click(fairx, fairy)
        time.sleep(3)
    elif int(choice) == 2:
        pyautogui.click(cheatx, cheaty)
        time.sleep(3)
    im_new = pyautogui.screenshot()

    if int(choice) == 0:
        if has_changed(heads1x, heads2x, heads1y, heads2y):
            heads += 1
        else:
            tails += 1
        flips -= 1
    elif int(choice) == 1 or int(choice) == 2:
        if has_changed(score1x, score2x, score1y, score2y):
            flips += 15
        else:
            flips -= 30

    print(heads, tails, flips)