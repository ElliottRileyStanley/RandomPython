import pyautogui
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\270000056\AppData\Local\Programs\Tesseract-OCR'
im1 = pyautogui.screenshot()

text = pytesseract.image_to_string(im1)
print(text)