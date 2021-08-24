
from tkinter import *


def exit():
	master.destroy()
master = Tk()
master.geometry("800x720+0+0")
master.config(bg='steelblue')
v = IntVar()
heading = Label(master, text="How are you?", bg='steelblue', fg='black', font='Times 24')
label_7 = Label(master, text=" Select any choice", width=20, font=("bold", 9))
label_7.place(x=180, y=135)

r3 = Radiobutton(master, text="YES", padx=10, value=1)
r3.place(x=200, y=185)
r4 = Radiobutton(master, text="NO", padx=30, value=2)
r4.place(x=350, y=185)

button = Button(master, text="EXIT", bg='yellow', command=exit, font="arial 8 bold")
heading.pack(side=TOP)
heading.place(x=195, y=30)
button.pack(side=TOP)
button.place(x=250, y=250)
mainloop()
