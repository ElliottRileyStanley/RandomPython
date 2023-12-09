import pyautogui

r = 0

while r != 43:
    im1 = pyautogui.screenshot()
    im2 = im1.convert('RGB')
    r,g,b = im2.getpixel((pyautogui.position()))
    print(r,g,b)
    if r == 75 and g == 219 and b == 106:
        pyautogui.click()
