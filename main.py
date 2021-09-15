from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog, messagebox
import time
import io

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
    l1 =Label(app, text = 'FILE PATH')
    l2 =Label(app, text = 'FILE NAME')
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    compiling = Button(app, text = 'RUN/ TEST',command = lambda: compilation())
    exe = Button(app, text = 'CONVERT TO EXE', command = lambda: py_exe())
    r1 = Radiobutton(app, text="WITH TERMINAL", variable=var, value=1, command = lambda:selection())
    r2 = Radiobutton(app, text="WITHOUT TERMINAL", variable=var, value=2, command = lambda: selection())
    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    # //////////////       Defining Functions        ////////////////////////
    def statements():
        text2.config(state=NORMAL)
        text2.insert(END, 'RUNNING THE PROGRAM\n')
        # text2.config(state=DISABLED)
    def selection():
        # print(str(var.get())
        print(str(var.get()))
        f = open("terminal_options.txt", "w")
        f.write(str(var.get()))
        f.close()

    def py_exe():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        inp1 = words.get()
        inp2 = file_words.get()
        try:
            # f = open(r"file_name.txt", "r")
            # filename = f.read()
            # f = open(r"file_path.txt", "r")
            # filepath = f.read()
            # f = open(r"terminal_options.txt", "r")
            # terminal = f.read()
            if inp2 == '' or inp2 == None or filepath == '' or filepath == None or terminal == '' or terminal == None:
                print('it is empty')
            else:
                text2.config(state=NORMAL)
                text2.insert(END, 'CONVERTING THE PROGRAM\n')
                if int(terminal) == 1:
                    text2.insert(END, 'CONVERTING THE PROGRAM ALONG WITH THE TERMINAL\n')
                    os.chdir(inp1)
                    os.system('pyinstaller --onefile '+inp2)
                elif int(terminal) == 2:
                    text2.insert(END, 'CONVERTING THE PROGRAM WITHOUT THE TERMINAL\n')
                    os.chdir(+inp1)
                    os.system('pyinstaller --onefile -w '+inp2)
                else:
                    text2.insert(END, 'PLEASE DO NOT EDIT THE FILE\n')
                # p = sub.Popen('cd '+filepath ,stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
                # output, errors = p.communicate()
                # text2.insert(END, output)
                # p = sub.Popen("python "+filename ,stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
                # output, errors = p.communicate()
                # text2.insert(END, output)
                text2.config(state=DISABLED) 
                
                # os.system('pyinstaller --onefile -w -i "path.ico" yourfile.py'+filename)
        except Exception as e:
            print(e)
            messagebox.showinfo("File Not Found!",  "We have observed in the deletion of file please stop tampering the files!")
            app.destroy()
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
            f = open("file_path.txt", "w")
            f.write(filep)
            f = open("file_name.txt", "w")
            f.write(new_filename)
            f.close()
            r1.select()
            r1.place( x = 500, y = 80)
            r2.place( x = 650, y = 80)
            text2.place(x = 220, y = 120, height = 300)
            compiling.place(x = 700, y = 450)
            exe.place(x = 800, y = 450)
        except Exception as e:
            f = open("file_path.txt", "w")
            f.write('')
            f = open("file_name.txt", "w")
            f.write('')
            words.config(state=NORMAL)
            words.delete(0, END)
            words.config(state=DISABLED)
            compiling.place_forget()
            exe.place_forget()
            text2.place_forget()
            r1.place_forget()
            r2.place_forget()
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
        # os.system('python test.py')
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)
    def installer():
        r1.place_forget()
        r2.place_forget()
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
    f = open("terminal_options.txt", "w")
    f.write('1')
    f.close()
    frame.place(x = 0, y = 0)
    install_module.place(x = 50, y = 20)
    convert.place(x = 50, y = 70)
    # app.attributes('-alpha', 0.85)
    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()