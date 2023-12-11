import pyautogui
import numpy

def calibrate_mouse():
    change = 100
    x, y = 0, 0
    pastx, pasty = 0, 0

    while change > 0:
        pastx, pasty = x, y
        x, y = pyautogui.position()
        change = change-0.01+abs(pastx-x)+abs(pasty-y)
    return x, y

def has_changed(startx, endx, starty, endy):
    for x in range(startx,endx):
        for y in range(starty,endy):
            if im_prev.convert('RGB').getpixel([x,y]) != im_new.convert('RGB').getpixel([x,y]):
                return True
    return False
    

headsx, headsy = calibrate_mouse()
tailsx, tailsy = calibrate_mouse()
flipx, flipy = calibrate_mouse()
im_prev = pyautogui.screenshot()
pyautogui.click(x=flipx, y=flipy)
im_new = pyautogui.screenshot()



if has_changed(1522, 1600, 263, 299):
    print("Heads")
elif has_changed(1506, 1567, 313, 343):
    print("Tails")
else:
    print("AAAAAAAAAAAA")