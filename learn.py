"""Aryabhatt - A Basic Math Learning Software """

from Tkinter import*
import tkMessageBox
#import subprocess
import os

root=Tk()
root.title("Aryabhatt-A Basic Math Learning Software")
root.geometry("670x340")

#Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-A Basic Math Learning Software",font=("Helvetica", 20),anchor=CENTER).grid(column=1,row=0,columnspan=7)

#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def ram():
     os.system("python learn1.py" )
     
     
def quit():
	'''
	Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
	'''
	choice = tkMessageBox.askyesno('Quit Application','Are you sure you wish to stop playing Aryabhatt! ?')
	if choice == True:
		root.destroy()
	elif choice == False:
		pass

    
button1=Button(root,text="LEARN",bg="blue",bd=5,fg="white",command=ram)
button1.grid(column=3,row=3)
button1.config( height = 10, width = 7)
button2=Button(root,text="TRY",bd=5,bg="pink",fg="blue",command=quit)
button2.grid(column=4,row=3)
button2.config( height = 10, width = 7)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=0,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
