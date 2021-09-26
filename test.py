# import time
# from tkinter import *


# app = Tk()
# b = Button(app, text = "hello", command = lambda: moving())
# def moving():
#     X,Y = 0,0
#     for i in range(50):
#         b.place(x=X,y=Y)
#         X=X+1
#         Y=Y+1
#         time.sleep(0.1)
# b.place(x= 10, y =10)
# app.mainloop()
import tkinter as tk

root = tk.Tk()
b = tk.Button(root, text="Example")

def move(i):
    if i<=50:
        b.place(x=i, y=i)
        b.after(20, lambda: move(i)) #after every 100ms
        i = i+1

move(0) #Start animation instantly
root.mainloop()