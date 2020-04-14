import threading
from tkinter import *
from PIL import Image, ImageTk
import math
import cv2
import time
def ImageDisplay(i):
    display = i;
    imagelist = ["display image/one.jpg", "display image/two2.jpg", "display image/three.jpg","display image/four.jpg","display image/five.jpg"]
    image1 = cv2.imread(imagelist[i])
    width = 640
    height = 480
    dim = (width, height)
    image = cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
    return image

def ImageChanger():
        for i in range(0, 5):
                print(i)
                cv2.imshow('display',ImageDisplay(i))
                time.sleep(10)
#threading.Thread(target=ImageChanger).start()

def Image2(i):
    canvas = Canvas(height=200,width=200)
    canvas.pack()
    canvas.delete("all")
    imagelist = ["display image/one.jpg", "display image/two2.jpg", "display image/three.jpg","display image/four.jpg","display image/five.jpg"]
    image1 = Image.open(imagelist[i])
    x, y = image1.size
    x2, y2 = math.floor(x-1100), math.floor(y-1100)
    image1 = image1.resize((x2,y2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    canvas.create_image(0,0,anchor='nw',image=photo)
    canvas.image = photo

for i in range(0, 5):
    print(i)
    Image2(i)
    time.sleep(10)
