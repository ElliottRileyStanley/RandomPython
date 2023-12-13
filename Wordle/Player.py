import pyautogui
import time

def find_edges(startx, starty, startcolor):
    edge_found = False
    search = startx
    while edge_found == False:
        search += 1
        if im.getpixel([search, starty]) != startcolor:
            edge_found = True
    right = search-2

    edge_found = False
    search = startx
    while edge_found == False:
        search -= 1
        if im.getpixel([search, starty]) != startcolor:
            edge_found = True
    left = search+2

    edge_found = False
    search = starty
    while edge_found == False:
        search -= 1
        if im.getpixel([startx, search]) != startcolor:
            edge_found = True
    top = search+2

    edge_found = False
    search = starty
    while edge_found == False:
        search += 1
        if im.getpixel([startx, search]) != startcolor:
            edge_found = True
    bottom = search-2

    return left, top

def get_state(guess, letter):
    global left, up
    im = pyautogui.screenshot()
    color = im.getpixel([left+difference*letter, up+difference*guess])
    return color

im = pyautogui.screenshot()
input("Put cursor in the top left square")
firstx, firsty = pyautogui.position()
input("Put cursor in the square to the right")
secondx, secondy = pyautogui.position()
startcolor = im.getpixel([firstx, firsty])

left = find_edges(firstx, firsty, startcolor)[0]
up = find_edges(firstx, firsty, startcolor)[1]

difference = find_edges(secondx, secondy, startcolor)[0]-left
left -= difference
up -= difference