from tkinter import *

root = Tk()
#b = Button(root)
#b['text'] = 'test'

#def test(event):
    #print('test click')

#b.bind('<Button-1>', test)
#b.pack()

c = Canvas(root, width=500, height=500, bg="lightblue", cursor="pencil")
c.create_polygon([250,100],[200,150],[300,150],fill="yellow")
c.pack()

root.mainloop()