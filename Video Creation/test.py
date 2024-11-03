from PIL import Image, ImageDraw
import cv2
import numpy

frames = []

result = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'MJPG'), 16, (1080, 1920))

for x in range(256):
    image = ImageDraw.Draw(Image.new("RGB", (1080, 1920)))
    image.rectangle([(0, 0), (1080, 1920)], fill= (x, x, x))
    result.write(cv2.cvtColor(numpy.array(image._image), cv2.COLOR_RGB2BGR))


result.release()