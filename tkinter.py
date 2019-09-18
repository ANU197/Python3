from tkinter import *
r = tkinter.Tk()
r.title('Counting Seconds')
button = tkinter.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
