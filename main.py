from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog, messagebox
import time
import io
temp = False
def main():
    output = ''
    # /////////////////   INITIALISING THE OBJECTS   //////////////////////////
    app = Tk()
    var = IntVar()
    text1 = Text(app)
    text2 = Text(app)
    text1.config(state=DISABLED)
    text2.config(state=DISABLED)
    b1 = Button(app, text= 'INSTALL MODULE', command = lambda: package_installer())
    words = Entry(app)
    words.config(state=DISABLED)
    file_words = Entry(app)
    file_words.config(state=DISABLED)
    file_icon = Entry(app)
    file_icon.config(state = DISABLED)
    l1 =Label(app, text = 'FILE PATH')
    l2 =Label(app, text = 'FILE NAME')
    ck = Checkbutton(app, text = 'LOGO', command = lambda: puticon())
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    icon_button = Button(app, text = 'ICON FILE', command = lambda: iconfile())
    compiling = Button(app, text = 'RUN/ TEST',command = lambda: compilation())
    exe = Button(app, text = 'CONVERT TO EXE', command = lambda: py_exe())
    r1 = Radiobutton(app, text="WITH TERMINAL", variable=var, value=1)
    r2 = Radiobutton(app, text="WITHOUT TERMINAL", variable=var, value=2)
    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    # //////////////       Defining Functions        ////////////////////////
    def iconfile():
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a ico file",filetypes=(("ICON FILES","*.ico"),("All files",'*')))
        try:
            if filename:
                filepath = os.path.abspath(filename.name)
                inp1 = words.get()
                try:
                    ic1, ic2 = filepath.split(inp1)
                except Exception:
                    ic2 = filepath
                # print(ic2)
            file_icon.config(state = NORMAL)
            file_icon.insert(0, ic2)
            file_icon.config(state = DISABLED)
        except Exception:
            file_icon.config(state = NORMAL)
            file_icon.delete(0, END)
            file_icon.config(state = DISABLED)
                # file_icon.delete()
    def puticon():
        global temp
        if temp:
            temp =False
            file_icon.place_forget()
            icon_button.place_forget()
            file_icon.config(state = NORMAL)
            file_icon.delete(0, END)
            file_icon.config(state = DISABLED)
        else:
            file_icon.place(x = 290, y = 80, width = 230)
            icon_button.place(x = 524,y = 80)
            temp= True
    def statements():
        text2.config(state=NORMAL)
        text2.insert(END, 'RUNNING THE PROGRAM\n')
        # text2.config(state=DISABLED)

    def py_exe():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        inp1 = words.get()
        inp2 = file_words.get()
        terminal = str(var.get())
        # print(terminal)
        icons = file_icon.get()
        # print(icons)
        if int(terminal) == 1 and len(icons) == 0:
            # print('only terminal')
            text2.insert(END, 'CONVERTING THE PROGRAM ALONG WITH THE TERMINAL\n')
            os.chdir(inp1)
            os.system('pyinstaller --onefile '+inp2)
        elif int(terminal) == 1 and len(icons) != 0:
            print('only terminal with icon')
            # text2.insert(END, 'CONVERTING THE PROGRAM ALONG WITH THE TERMINAL\n')
            # os.chdir(inp1)
            # os.system('pyinstaller --onefile '+inp2)
            # os.system('pyinstaller --onefile -w -i "path.ico" yourfile.py'+filename)
        elif int(terminal) == 2 and len(icons) == 0:
            # print('without terminal')
            text2.insert(END, 'CONVERTING THE PROGRAM WITHOUT THE TERMINAL\n')
            os.chdir(inp1)
            os.system('pyinstaller --onefile -w '+inp2)
        elif int(terminal) == 2 and len(icons) != 0:
            print('without terminal with icon')
            # text2.insert(END, 'CONVERTING THE PROGRAM WITHOUT THE TERMINAL\n')
            # os.chdir(inp1)
            # os.system('pyinstaller --onefile -w '+inp2)
            # os.system('pyinstaller --onefile -w -i "path.ico" yourfile.py'+filename)
        else:
            text2.insert(END, 'PLEASE DO NOT EDIT THE FILE\n')
                
    def openfile():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a Python file",filetypes=(("Python files","*.py"),("All files",'*')))
        try:
            if filename:
                filepath = os.path.abspath(filename.name)
            new_filename = os.path.basename(filepath)
            fp = filepath.split(new_filename)
            filep = fp[0]
            words.config(state=NORMAL)
            words.insert(0, filep)
            words.config(state=DISABLED)
            file_words.config(state=NORMAL)
            file_words.insert(0, new_filename)
            # inp = file_words.get()
            file_words.config(state=DISABLED)
            # print(inp)
            r1.select()
            r1.place( x = 600, y = 80)
            r2.place( x = 750, y = 80)
            ck.place(x = 220, y = 80)
            text2.place(x = 220, y = 120, height = 300)
            compiling.place(x = 700, y = 450)
            exe.place(x = 800, y = 450)
        except Exception as e:
            words.config(state=NORMAL)
            words.delete(0, END)
            words.config(state=DISABLED)
            file_words.config(state=NORMAL)
            file_words.delete(0, END)
            file_words.config(state=DISABLED)
            compiling.place_forget()
            exe.place_forget()
            text2.place_forget()
            r1.place_forget()
            r2.place_forget()
            ck.place_forget()
    def compilation():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        inp1 = words.get()
        inp2 = file_words.get()
        print(inp1, inp2)
        print(str(var.get()))
        text2.config(state=NORMAL)
        text2.insert(END, 'RUNNING THE PROGRAM\n')
        text2.insert(END, 'COMPILED SUCCESSFULLY!\n')
        text2.config(state=DISABLED)
        os.chdir(inp1)
        os.system('python '+inp2)
    def package_installer():
        text1.config(state=NORMAL)
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)
    def installer():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)
        file_words.config(state=NORMAL)
        file_words.delete(0, END)
        file_words.config(state=DISABLED)
        icon_button.place_forget()
        file_icon.place_forget()
        r1.place_forget()
        r2.place_forget()
        ck.place_forget()
        compiling.place_forget()
        exe.place_forget()
        l1.place_forget()
        l2.place_forget()
        words.place_forget()
        file_words.place_forget()
        open_button.place_forget()
        text2.place_forget()
        text1.place(x = 220, y = 10)
        b1.place(x = 460, y = 400)
    def converter():
        text1.place_forget()
        b1.place_forget()
        l1.place(x= 220, y = 10)
        l2.place(x= 650, y = 10)
        open_button.place(x = 800, y = 40)
        words.place(x = 220, y = 40, width = 400)
        file_words.place(x = 650, y = 40, width = 140)
    
    frame.place(x = 0, y = 0)
    install_module.place(x = 50, y = 20)
    convert.place(x = 50, y = 70)
    # app.attributes('-alpha', 0.85)
    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()