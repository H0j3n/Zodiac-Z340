import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((300,400,3),np.uint8)
b,g,r,a = 0,255,0,0

## Use simsum.ttc to write Chinese.
fontpath = "./z340-z408.ttf"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 100),  "+@.jYpFG7(N^RFkO", font = font, fill = (b, g, r, a))
draw.text((50, 150),  "+@.jYpFG7(N^RFkO", font = font, fill = (b, g, r, a))
img = np.array(img_pil)

## Display 
cv2.imwrite("res.png", img)
