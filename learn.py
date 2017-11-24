"""Aryabhatt - A Basic Math Learning Software """
import os
from Tkinter import*
import tkMessageBox
#import subprocess


root=Tk()
root.title("Aryabhatt-A Basic Science Learning Software")
root.geometry("670x340")

#Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-A Basic Science Learning Software",font=("Helvetica", 18),anchor=CENTER).grid(column=1,row=1,columnspan=7)

#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def ram():
	 root.destroy()
	 os.system('python learn1.py')
	 
def about():
	'''
	Load the About Info Box.
	'''
        tkMessageBox.showinfo("About Aryabhatt!","Welcome to Aryabhatt! v0.1\n Aryabhatt is developed to explore Tkinter and then started off as a simple application.\nAryabhatt! is maintained at \nhttps://github.com/jervis446/Aryabhatt/ \n\nYour contributions and suggestions are welcome. Feel free to fork and pull changes to Aryabhatt! The application is open-source and is open for development.\n\nAryabhatt is developed and maintained by Adarsh kumar. For suggestions and changes, feel free to drop an email:\n kumar[dot]adarshluv99[at]gmail[dot]com .\n\nInitial Release: Nov '17.")
       

def quix():
	root.destroy()
	os.system('python quiz.py')

     
def quit():
	'''
	Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
	'''
	choice = tkMessageBox.askyesno('Quit Application','Are you sure you wish to stop playing Aryabhatt! ?')
	if choice == True:
		root.destroy()
	elif choice == False:
		pass

button8=Button(root,text="About",bg="black",fg="white",command=about)
button8.grid(column=0,row=0)
button8.config( height = 1, width = 2)

button8=Button(root,text="Quit",bg="red",fg="black",command=quit)
button8.grid(column=8,row=0)
button8.config( height = 1, width = 2)
    
button1=Button(root,text="LEARN",bg="blue",bd=5,fg="white",command=ram)
button1.grid(column=3,row=3)
button1.config( height = 10, width = 7)
button2=Button(root,text="TRY",bd=5,bg="pink",fg="blue",command=quix)
button2.grid(column=4,row=3)
button2.config( height = 10, width = 7)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=0,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
