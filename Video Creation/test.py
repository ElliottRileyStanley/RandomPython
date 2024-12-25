from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy

start_color = (0, 0, 0)
start_name = "Black"
end_color = (255, 0, 255)
end_name = "Neon Pink"

font = ImageFont.truetype(r'C:\Users\Ellio\OneDrive\Desktop\Coding\Python\Random\Video Creation\ELEGANTTYPEWRITER.ttf', 20)

result = cv2.VideoWriter(r'Video Creation\video.avi', cv2.VideoWriter_fourcc(*'MJPG'), 60, (1080, 1920))

for x in range(360):
    image = ImageDraw.Draw(Image.new("RGB", (1080, 1920)))
    
    r = round((end_color[0] * x/359) + (start_color[0] * (359-x)/359))
    g = round((end_color[1] * x/359) + (start_color[1] * (359-x)/359))
    b = round((end_color[2] * x/359) + (start_color[2] * (359-x)/359))

    image.rectangle([(0, 0), (1080, 1920)], fill= (r, g, b))

    w = image.textlength(start_name, font)

    image.text((540 - w, 900), start_name, font = font, fill = (255, 255, 255), align = "center")
    image.text((540, 960), "to", font = font, fill = (255, 255, 255), align = "center")
    image.text((540, 960), end_name, font = font, fill = (255, 255, 255), align = "center")

    result.write(cv2.cvtColor(numpy.array(image._image), cv2.COLOR_RGB2BGR))

result.release()
