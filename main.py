from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog
output = ''

def main():
    # /////////////////   INITIALISING THE OBJECTS   //////////////////////////
    app = Tk()
    text1 = Text(app)
    b1 = Button(app, text= 'INSTALL MODULE', command = lambda: package_installer())
    words = Entry(app)
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    # //////////////       Defining Functions        ////////////////////////
    def openfile():
        words.delete(0, END)
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a Python file",filetypes=(("Python files","*.py"),("All files",'*')))
        if filename:
          filepath = os.path.abspath(filename.name)

        print(filepath)
        filename = os.path.basename(filepath)
        print(filename)
        fp = filepath.split(filename)
        print(fp[0])
        words.insert(0, filepath)
    
    def package_installer():
        # os.system('python test.py')
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        text1.insert(END, output)

    def installer():
        words.place_forget()
        open_button.place_forget()
        text1.place(x = 220, y = 10)
        b1.place(x = 460, y = 400)

    def converter():
        open_button.place(x = 400, y = 40)
        words.place(x = 220, y = 10, width = 400)
        text1.place_forget()
        b1.place_forget()
    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())

    frame.place(x = 0, y = 0)
    install_module.place(x = 50, y = 20)
    convert.place(x = 50, y = 70)

    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()