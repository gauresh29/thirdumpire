"""
simple project in python 

This project is third upire review system 
date 11/11/2021
"""
import tkinter
from tkinter.constants import ANCHOR, NW
import cv2 #pip install open cv python 
import PIL.Image, PIL.ImageTk #pip install pil
from functools import partial
import threading
import imutils #pip install imutils
import time 

stream = cv2.VideoCapture("clip1.mp4")
flag = True
def play(speed):
    print(f"speed is {speed}")
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed, frame = stream.read()
    if not grabbed:
        exit()

    frame = imutils.resize(frame, width=SET_WIDTH , height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame , anchor = tkinter.NW)
    if flag:
        canvas.create_text(140,27,fill="red",font="time 26 bold", text="decision pending")
    flag = not flag

def pending(decision):
    
    #1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH, height= SET_HEIGHT )
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)
    #2. wait for one second
    time.sleep(1)
    #3 .Display sponser image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH, height= SET_HEIGHT )
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)
    #4. wait for 2 second
    time.sleep(2)
    #5. Display out/notout image 
    if decision == "out" :
        decisionimg = "out.png"
    else :
        decisionimg = "not_out.png"

    frame = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH, height= SET_HEIGHT )
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)  
    
def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def notOut():
    thread = threading.Thread(target=pending,args=("notOut",))
    thread.daemon = 1
    thread.start()
    print(f"Not out")


SET_WIDTH = 650
SET_HEIGHT = 368

window = tkinter.Tk()
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width= SET_WIDTH , height= SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho = tkinter.NW , image = photo)
canvas.pack()

#buttons 
btn = tkinter.Button(window, text="<< previous(fast)", width=50,command=partial(play,-25))
btn.pack()
btn = tkinter.Button(window, text="<< previous(slow)", width=50,command=partial(play,-2))
btn.pack()
btn = tkinter.Button(window, text=">> next(fast)", width=50,command=partial(play,25))
btn.pack()
btn = tkinter.Button(window, text=">>next(slow)", width=50, command=partial(play,2))
btn.pack()
btn = tkinter.Button(window, text="Give out", width=50,command=out)
btn.pack()
btn = tkinter.Button(window, text="Give not out", width=50,command=notOut)
btn.pack()

window.title("Gauresh third umpire decision system")
window.mainloop()
