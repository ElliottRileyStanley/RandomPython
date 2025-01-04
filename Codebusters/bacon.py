import random

alphabet = {
    "a": [False, False, False, False, False],
    "b": [False, False, False, False, True],
    "c": [False, False, False, True, False],
    "d": [False, False, False, True, True],
    "e": [False, False, True, False, False],
    "f": [False, False, True, False, True],
    "g": [False, False, True, True, False],
    "h": [False, False, True, True, True],
    "i": [False, True, False, False, False],
    "j": [False, True, False, False, False],
    "k": [False, True, False, False, True],
    "l": [False, True, False, True, False],
    "m": [False, True, False, True, True],
    "n": [False, True, True, False, False],
    "o": [False, True, True, False, True],
    "p": [False, True, True, True, False],
    "q": [False, True, True, True, True],
    "r": [True, False, False, False, False],
    "s": [True, False, False, False, True],
    "t": [True, False, False, True, False],
    "u": [True, False, False, True, True],
    "v": [True, False, False, True, True],
    "w": [True, False, True, False, False],
    "x": [True, False, True, False, True],
    "y": [True, False, True, True, False],
    "z": [True, False, True, True, True],
    " ": [True, True, True, False, True],
    ",": [True, True, True, True, False],
    ".": [True, True, True, True, True]
}

def bacon(message):
    result = []
    for i in range(len(message)):
        result += alphabet[message[i].lower()]
    
    while len(result) < 1100:
        result += [True, False, True, False, True]
    return result

