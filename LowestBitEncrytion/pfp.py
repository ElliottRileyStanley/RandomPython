from PIL import Image
import numpy as np
import qrcode
import qrcode.constants
import random

qr = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data("You search so far, for nothing")

matrix = qr.get_matrix()


pfp = Image.new(mode="RGB", size=(25, 25), color=(0, 0, 0))

edit = pfp.load()

for x in range(25):
    for y in range(25):
        if not(matrix[x][y]):
            edit[x, y] = (1, random.randrange(150, 255), random.randrange(150, 255))
        else:
            edit[x, y] = (0, random.randrange(150, 255), random.randrange(150, 255))


pfp = pfp.resize((100, 100), resample=Image.Resampling.NEAREST)
pfp.save("LowestBitEncrytion\PFP.PNG")
