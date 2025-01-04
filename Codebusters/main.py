from PIL import Image
from bacon import *

im = Image.new(mode="RGB", size=(85, 110), color=(255, 255, 255))

edit = im.load()

message = "A baconian cipher involves choosing two symbols, or groups of symbols, and using them to show characters through binary encoding. The symbols can range from emojis, hieroglyphs, and even different parts of the alphabet."

encoded = bacon(message)

index = 0
for y in range(0, 110):
    for x in range(0, 5):
        if encoded[index]:
            edit[x, y] = (0, 0, 0)
        index += 1

for y in range(0, 110):
    for x in range(80, 85):
        if encoded[index]:
            edit[x, y] = (0, 0, 0)
        index += 1

im = im.resize((850, 1100), resample=Image.NEAREST)
im.save(r'Codebusters\output.png')