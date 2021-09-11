from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog
output = ''

def main():
    app = Tk()
    def openfile():
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a file",filetypes=(("txt files","*.txt"),("All files",'*')))
        print(filename)
    
    text1 = Text(app)
    b1 = Button(app, text= 'INSTALL MODULE')
    words = Entry(app)
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())

    def installer():
        words.place_forget()
        open_button.place_forget()
        text1.place(x = 220, y = 10)
        # b1 = Button(app, text= 'INSTALL MODULE', command = lambda: test())
        b1.place(x = 460, y = 400)
    def converter():
        open_button.place(x = 300, y = 10)
        words.place(x = 220, y = 10)
        text1.place_forget()
        b1.place_forget()
    # def test():
    #     # os.system('python test.py')
    #     p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE)
    #     output, errors = p.communicate()
    #     text.insert(END, output)
    


    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    frame.place(x = 0, y = 0)

    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    install_module.place(x = 50, y = 20)
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    convert.place(x = 50, y = 70)

    
    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()