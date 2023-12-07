import pyautogui
import time

word_list = open(r"Anagram\organized_dictionary.text").readlines()

game_type = input("Game 1/2")

def check_word(word):
    letters = "aeydrdedx"
    if game_type == "2" and letters[4] not in word:
        return False
    for letter in word:
        if letter not in letters:
            return False
        letters = letters.replace(letter, "", 1)
    pyautogui.write(word)
    pyautogui.press('enter')
    return True

result = []

time.sleep(3)

for word in word_list:
    word = word[0:len(word)-1]
    if check_word(word) == True:
        result.append(word)

print(result)