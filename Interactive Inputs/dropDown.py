
from tkinter import *


def exit():
	master.destroy()
master = Tk()
master.geometry("800x720+0+0")
master.config(bg='steelblue')
v = IntVar()
heading = Label(master, text="How are you?", bg='steelblue', fg='black', font='Times 24')
label_7 = Label(master, text=" Select your favourite color", width=25, font=("bold", 9))
label_7.place(x=180, y=135)



variable = StringVar(master)
variable.set("Select") # default value

w = OptionMenu(master, variable, "Red", "Yellow", "Blue","Pink","Green")
w.pack()
w.place(x=250,y=180)


button = Button(master, text="EXIT", bg='yellow', command=exit, font="arial 8 bold")
heading.pack(side=TOP)
heading.place(x=195, y=30)
button.pack(side=TOP)
button.place(x=250, y=400)
mainloop()
