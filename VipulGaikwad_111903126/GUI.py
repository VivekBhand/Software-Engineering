from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
#window.geometry("200x100")  
  
b = Button(window,text = "Simple")  
  
b.pack()  
window.mainloop()
