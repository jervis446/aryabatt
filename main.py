"""Aryabatt - A Basic Math Learning Software """

from Tkinter import*

root=Tk()
root.title("Aryabhatt-A Basic Math Learning Software")
root.geometry("670x340")

Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-A Basic Math Learning Software",font=("Helvetica", 20)).grid(column=0,row=1,columnspan=9)


#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def insert(x):
    
    e.insert(END,x)
def clear():
    e.delete(0,END)
def result(x):
    y=eval(e.get())
    clear()
    e.insert(END,y)
def clearr():
    value=e.get()
    value=value[:-1]
    e.delete(0,END)
    e.insert(0,value)
    
Button(root,text="ENTER",bd=5,fg="blue",command=lambda:insert('-')).grid(column=4,row=3)

Button(root,text="QUIT",bd=5,fg="red",command=quit).grid(column=4,row=4)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=0,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
