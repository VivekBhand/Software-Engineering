from tkinter import *  
window = Tk()  
heading = Label(window, text="Welcome", bg='white', fg='black', font='Times 24')
heading.pack(side=TOP)
heading.place(x=25, y=30)
username = Button(window, text="Username", bg='yellow', font="arial 8 bold")
username.pack(side=LEFT)
username.place(x=30, y=70)
userbox = Entry(window)
userbox.pack(side=RIGHT)
userbox.place(x=110, y=70)
password = Button(window, text="Password", bg='yellow', font="arial 8 bold")
password.pack(side=LEFT)
password.place(x=30, y=100)
passbox = Entry(window)
passbox.pack(side=RIGHT)
passbox.place(x=110, y=100)
window.mainloop()  
