from tkinter import *
from datetime import date


window = Tk()
window.title("My First App")
window.geometry("500x400")
window.configure(bg="Orange")

lbll = Label(window,text="Hi Everyone!", bg="black", fg="white", height=2, width=400)
lbll.pack()

name_lbl = Label(window, text="Full name", font=("Times New Roman", 12))
name_entry = Entry(window)

name_lbl.pack()
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message =" Welcome to the Application! \nToday's date is:"
    greet = "Hello "+ name
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert
    text_box.insert(END,date.today())


btn = Button(window, text = "begin", bg="blue", fg="white", height=1, width=10, command=display)
btn.pack()

text_box = Text(window, height=3,width=40)
text_box.pack()






window.mainloop()