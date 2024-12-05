from tkinter import *

master = Tk()

greeting = Label(master, text="Hello User", fg='black', bg='white')
greeting.pack()

button = Button(master, text="Click me", fg='black', bg='white')
button.pack()

entry = Entry(master, fg="yellow", bg="blue", width=50)
entry.pack()

frame = Frame(master, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="Sample Frame")
label.pack()

master.mainloop()