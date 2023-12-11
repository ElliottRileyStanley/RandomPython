import pyautogui


im1 = pyautogui.screenshot()
for pos in pyautogui.locateAllOnScreen(r'Primer\3_primer.png', confidence=0.8):
    print(pos)