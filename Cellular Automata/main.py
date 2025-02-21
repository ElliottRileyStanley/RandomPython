from PIL import Image
import numpy as np
import random

width, height = 300, 480
numFrames = 5

def new_frame(old):
    new = [[0 for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            alive_neighbors = 0

            alive_neighbors += old[(x - 1) % width][(y - 1) % height]
            alive_neighbors += old[(x - 1) % width][(y) % height]
            alive_neighbors += old[(x - 1) % width][(y + 1) % height]
            alive_neighbors += old[(x) % width][(y - 1) % height]
            alive_neighbors += old[(x) % width][(y + 1) % height]
            alive_neighbors += old[(x + 1) % width][(y - 1) % height]
            alive_neighbors += old[(x + 1) % width][(y) % height]
            alive_neighbors += old[(x + 1) % width][(y + 1) % height]

            if old[x][y] == 1:
                if alive_neighbors >=1 and alive_neighbors <= 5:
                    new[x][y] = 1
            elif old[x][y] == 0:
                if alive_neighbors == 3:
                    new[x][y] = 1
    return new

def printArray(array):
    for x in range(width):
        for y in range(height):
            print(array[x][y], end="")
        print()

def generateImage(array):
    return Image.fromarray(np.array(array, dtype='uint8') * 50, mode='L')



array = [[random.randint(0, 1) for _ in range(height)] for _ in range(width)]
frames = [generateImage(array)]

for i in range(numFrames):
    array = new_frame(array)
    frames.append(generateImage(array))

frames[numFrames-1].resize((1920, 1200), resample=Image.Resampling.NEAREST).save(r'Cellular Automata\output.png')