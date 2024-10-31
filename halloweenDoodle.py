import pyautogui
import keyboard

centerX = 1921
centerY = 595
sleep = 0.05

def hLine():
    pyautogui.moveTo(centerX - 50, centerY)
    pyautogui.mouseDown()
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX + 50, centerY)
    pyautogui.mouseUp()

def vLine():
    pyautogui.moveTo(centerX, centerY - 50)
    pyautogui.mouseDown()
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX, centerY + 50)
    pyautogui.mouseUp()

    

def upArrow():
    pyautogui.moveTo(centerX - 50, centerY + 50)
    pyautogui.mouseDown()
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX, centerY - 50)
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX + 50, centerY + 50)
    pyautogui.mouseUp()

def downArrow():
    pyautogui.moveTo(centerX - 50, centerY - 50)
    pyautogui.mouseDown()
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX, centerY + 50)
    pyautogui.sleep(sleep)
    pyautogui.moveTo(centerX + 50, centerY - 50)
    pyautogui.mouseUp()



keyboard.add_hotkey('4', hLine, args = ())
keyboard.add_hotkey('6', vLine, args = ())
keyboard.add_hotkey('8', upArrow, args = ())
keyboard.add_hotkey('2', downArrow, args = ())

keyboard.wait('esc')