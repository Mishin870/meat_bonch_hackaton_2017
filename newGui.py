from tkinter import *

root = Tk()
b = Button(root)
b['text'] = 'test'

def test(event):
    import test

b.bind('<Button-1>', test)
b.pack()

root.mainloop()