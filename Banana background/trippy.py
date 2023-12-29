import ctypes
import os
import time

for frame in range(0, 100000):
    src = r'trippy\ezgif-4-e86ad38ec4-gif-png\frame_' + str((frame % 7) + 1) + '_delay-0.1s.png'
    ctypes.windll.user32.SystemParametersInfoW(0x14, 0, os.path.abspath(src), 0x2)
    time.sleep(0.2)