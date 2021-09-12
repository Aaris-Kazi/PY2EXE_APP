from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog
import time
import io

the_com_file_path = ''
the_com_file = ''
def main():
    output = ''
    
    # /////////////////   INITIALISING THE OBJECTS   //////////////////////////
    app = Tk()
    text1 = Text(app)
    b1 = Button(app, text= 'INSTALL MODULE', command = lambda: package_installer())
    words = Entry(app)
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    

    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    # //////////////       Defining Functions        ////////////////////////

    def openfile():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)

        filep, new_filename= '', ''
        
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a Python file",filetypes=(("Python files","*.py"),("All files",'*')))
        try:
            print("file name",filename)
            if filename:
                filepath = os.path.abspath(filename.name)
                print('openfile: '+filepath)

            # print(filepath)
            words.config(state=NORMAL)
            words.insert(0, filepath)
            words.config(state=DISABLED)
            new_filename = os.path.basename(filepath)
            print(new_filename)
            fp = filepath.split(new_filename)
            filep = fp[0]
            print(filep)
            print(type(filep))
            compiling = Button(app, text = 'RUN/ TEST', command = lambda: compilation(filep, new_filename))
            if filename == 'None' or filename == '':
                compiling.place_forget()
            compiling.place(x = 460, y = 240)
        except Exception as e:
            filep, new_filename= '', None
            print('file is none', e)
            words.config(state=NORMAL)
            words.delete(0, END)
            words.config(state=DISABLED)
        
            
            
    def compilation(filep, new_filename):
        if new_filename == '' or new_filename == None or filep == '' or filep == None:
            print('Unable to proceed ahead')
        else:
            print(filep)
            print(new_filename)
            # n = str(fp[0])
            # print('cd '+filep)
            os.system('cd '+filep)
            os.system('python '+new_filename)

    def package_installer():
        text1.config(state=NORMAL)
        # os.system('python test.py')
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)

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

    frame.place(x = 0, y = 0)
    install_module.place(x = 50, y = 20)
    convert.place(x = 50, y = 70)

    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()