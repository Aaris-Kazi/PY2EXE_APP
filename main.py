from tkinter import *
import os
import subprocess as sub

output = ''

def main():
    app = Tk()
    
    text = Text(app)
    text.pack()
    
    def test():
        # os.system('python test.py')
        p = sub.Popen('pip install pyinstaller',stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        text.insert(END, output)
    

    b1 = Button(app, text= 'Transform', command = lambda: test())
    b1.pack()

    
    app.title('Transformer')
    app.geometry('720x480')
    app.mainloop()

if __name__ == '__main__':
    main()