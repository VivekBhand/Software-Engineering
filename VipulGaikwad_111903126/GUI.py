from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")

c = Button(window,text = "Hard")  
c.pack()

b = Button(window,text = "Simple")

b.pack() 
  
window.mainloop()
