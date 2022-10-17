from io import BytesIO
import requests
import urllib.request
from PIL import Image


img=input("Enter image link that you want to pixelise: ")

img = urllib.request.urlopen(img)
data=BytesIO(img.read())
img=Image.open(data)		
img = img.resize(
(img.size[0] // pixel_size, img.size[1] // pixel_size),Image.NEAREST)
img = img.resize((img.size[0] * pixel_size, img.size[1] * pixel_size),Image.NEAREST)

img.show()
img.save("pixelised.py)


