from tkinter import *
import os

def test():
    os.system('python test.py')
    # print('Hello world')

def main():
    app = Tk()

    b1 = Button(app, text= 'Transform', command = lambda: test())
    b1.pack()


    app.title('Transformer')
    app.geometry('720x480')
    app.mainloop()

if __name__ == '__main__':
    main()