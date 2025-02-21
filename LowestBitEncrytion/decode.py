from PIL import Image
import numpy as np

input = Image.open("LowestBitEncrytion\PFP.PNG")
input = input.resize((25, 25), resample=Image.Resampling.NEAREST)
output = Image.new(mode="RGB", size=(25, 25), color=(0, 0, 0))
output_edit = output.load()

input = np.array(input)

for x in range(25):
    for y in range(25):
        if input[x, y][0] == 1:
            output_edit[x, y] = (255, 255, 255)

output.save("LowestBitEncrytion\Decode.PNG")