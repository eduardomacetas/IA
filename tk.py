from Tkinter import *

root = Tk()

h = Scrollbar(root, orient=HORIZONTAL)
v = Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 500, 500), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_oval((lastx,lasty, lastx+5, lasty+5), fill=color)
    
    lastx, lasty = x, y
    if(color=="red"):
        print lastx, lasty,0
    if(color=="blue"):
        print lastx, lasty,1

def doneStroke(event):
    canvas.itemconfigure('currentline', width=5) # What happens if you set this to another number?        
        
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))

setColor("red")
canvas.itemconfigure('palette', width=5)
root.mainloop()