"""Aryabhatt - A Basic Math Learning Software """
import os
from Tkinter import*
import tkMessageBox
#import subprocess

root=Tk()
root.title("Aryabhatt-A Basic Math Learning Software")
root.geometry("670x340")

Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-A Basic Math Learning Software",font=("Helvetica", 20)).grid(column=0,row=1,columnspan=9)


#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def ram():
     root.destroy()
     os.system('python login.py')
     #subprocess.call("python quiz.py" )
     
     
def quit():
	'''
	Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
	'''
	choice = tkMessageBox.askyesno('Quit Application','Are you sure you wish to stop playing Aryabhatt! ?')
	if choice == True:
		root.destroy()
	elif choice == False:
		pass
     

   
    

    
Button(root,text="ENTER",bd=5,fg="blue",command=ram).grid(column=4,row=3)

Button(root,text="QUIT",bd=5,fg="red",command=quit).grid(column=4,row=4)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=0,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
