import pyautogui

with open("Colorfle\Choices.txt", "r") as file:
    choices = file.read()
    print(choices[0])

change = 0
x, y = 0, 0
pastx, pasty = 0, 0

while change > 0:
    pastx, pasty = x, y
    x, y = pyautogui.position()
    change = change-0.15+abs(pastx-x)+abs(pasty-y)
    print(change)

im1 = pyautogui.screenshot()
im2 = im1.convert('RGB')
r,g,b = im2.getpixel((pyautogui.position()))
print(r,g,b)