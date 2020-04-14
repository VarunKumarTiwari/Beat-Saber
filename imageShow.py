from tkinter import *
from PIL import Image, ImageTk
import math
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
root = Tk()

prompt = StringVar()
root.title("AVATAR")
label = Label(root, fg='dark green')
label.pack()

frame = Frame(root,background='red')
frame.pack()

# Function definition

# first create the canvas
#canvas = Canvas(height=200,width=200)
#canvas.pack()

def Image1(event):
    canvas.delete("all")
    image1 = Image.open("H:/Beat-Saber/display image/two2.jpg")
    x, y = image1.size
    x2, y2 = math.floor(x-400), math.floor(y-400)
    image1 = image1.resize((x2,y2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    canvas.create_image(0,0,anchor='nw',image=photo)
    canvas.image = photo

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
def Image3():
    canvas.delete("all")
    image1 = Image.open("H:/Beat-Saber/display image/three.jpg")
    x, y = image1.size
    x2, y2 = math.floor(x-1100), math.floor(y-1100)
    image1 = image1.resize((x2,y2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    canvas.create_image(0,0,anchor='nw',image=photo)
    canvas.image = photo
def Image4():
    canvas.delete("all")
    image1 = Image.open("H:/Beat-Saber/display image/four.jpg")
    x, y = image1.size

    x2, y2 = math.floor(x-1100), math.floor(y-1100)

    image1 = image1.resize((x2,y2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    canvas.create_image(0,0,anchor='nw',image=photo)
    canvas.image = photo
    
def Image5():
    canvas.delete("all")
    image1 = Image.open("H:/Beat-Saber/display image/five.jpg")
    x, y = image1.size
    x2, y2 = math.floor(x-1100), math.floor(y-1100)
    image1 = image1.resize((x2,y2),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    canvas.create_image(0,0,anchor='nw',image=photo)
    
    canvas.image = photo
#Invoking through


for i in range(0, 5):
    print(i)
    Image2(i)
    time.sleep(10)   
'''conversationbutton = Button(frame, text='Start    Conversation',width=25,fg='green',command = Image3)
conversationbutton.pack(side = RIGHT)

stopbutton = Button(frame, text='Stop',width=25,fg='red',command = Image5)
stopbutton.pack(side = RIGHT)

'''


root.mainloop()


