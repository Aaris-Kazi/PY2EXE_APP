from tkinter import *
import os
import subprocess as sub
from threading import Thread
from tkinter import filedialog, messagebox
import time
import io

filep = ''
new_filename = ''
def main():
    output = ''
    # /////////////////   INITIALISING THE OBJECTS   //////////////////////////
    app = Tk()
    text1 = Text(app)
    text2 = Text(app)
    text1.config(state=DISABLED)
    text2.config(state=DISABLED)
    b1 = Button(app, text= 'INSTALL MODULE', command = lambda: package_installer())
    words = Entry(app)
    words.config(state=DISABLED)
    open_button = Button(app, text = 'OPEN FILE', command = lambda: openfile())
    compiling = Button(app, text = 'RUN/ TEST',command = lambda: compilation())
    exe = Button(app, text = 'CONVERT TO EXE', command = lambda: py_exe())
    # //////////////////   BY DEFAULT INITIALISATION ON THE SCREEN ////////////////////
    frame = Frame(app, width= 200, height = 480, bg = 'blue')
    install_module = Button(app, text = 'INSTALL MODULES', command = lambda: installer())
    convert = Button(app, text = 'CONVERT TO EXE   ', command = lambda: converter())
    # //////////////       Defining Functions        ////////////////////////
    def py_exe():
        print('Hello')
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.insert(0, 'CONVERTING PY TO EXE')
        text2.config(state = DISABLED)
    def openfile():
        words.config(state=NORMAL)
        words.delete(0, END)
        words.config(state=DISABLED)
        
        filename=filedialog.askopenfile(initialdir='GUI/',title="Select a Python file",filetypes=(("Python files","*.py"),("All files",'*')))
        try:
            if filename:
                filepath = os.path.abspath(filename.name)
            
            words.config(state=NORMAL)
            words.insert(0, filepath)
            words.config(state=DISABLED)
            new_filename = os.path.basename(filepath)
            print(filepath)
            print(new_filename)
            fp = filepath.split(new_filename)
            filep = fp[0]
            f = open("file_path.txt", "w")
            f.write(filep)
            f = open("file_name.txt", "w")
            f.write(new_filename)
            f.close()
            text2.place(x = 220, y = 80, height = 350)
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
    def compilation():
        text2.config(state=NORMAL)
        text2.delete('1.0', END)
        text2.config(state = DISABLED)
        try:
            f = open(r"file_name.txt", "r")
            filename = f.read()
            f = open(r"file_path.txt", "r")
            filepath = f.read()
            if filename == '' or filename == None or filepath == '' or filepath == None:
                print('it is empty')
            else:
                text2.config(state=NORMAL)
                # text2.delete(0, END)
                text2.insert(END, 'RUNNING THE PROGRAM\n')
                pathing = r"C:\Users\aaris\Desktop\Pithooooon\PY2EXE_APP"
                p = sub.Popen('cd '+filepath ,stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
                output, errors = p.communicate()
                text2.insert(END, output)
                p = sub.Popen("python "+filename ,stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
                output, errors = p.communicate()
                text2.insert(END, output)
                text2.config(state=DISABLED)
                # os.system("start cmd /c {command here}")  
                # os.system('cd '+filepath)
                # os.system('python '+filename)
                # os.remove("file_name.txt")
                # os.remove("file_path.txt")
        except Exception as e:
            # print(e)
            messagebox.showinfo("File Not Found!",  "We have observed in the deletion of file please stop tampering the files!")
            app.destroy()
    def package_installer():
        text1.config(state=NORMAL)
        # os.system('python test.py')
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE, shell= True)
        output, errors = p.communicate()
        text1.insert(END, output)
        text1.config(state=DISABLED)
    def installer():
        compiling.place_forget()
        exe.place_forget()
        words.place_forget()
        open_button.place_forget()
        text2.place_forget()
        text1.place(x = 220, y = 10)
        b1.place(x = 460, y = 400)
    def converter():
        text1.place_forget()
        b1.place_forget()
        open_button.place(x = 400, y = 40)
        words.place(x = 220, y = 10, width = 400)
    
    frame.place(x = 0, y = 0)
    install_module.place(x = 50, y = 20)
    convert.place(x = 50, y = 70)

    app.title('Transformer')
    app.geometry('920x480')
    app.mainloop()

if __name__ == '__main__':
    main()