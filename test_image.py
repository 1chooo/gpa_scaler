from PIL import Image
import pytesseract
import os


path = os.getcwd()
path += "/imgs/1091.png"
print(path)

img = Image.open(path)
text = pytesseract.image_to_string(img, lang='eng')
print(text)
