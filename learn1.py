"""Aryabhatt - A Basic Math Learning Software """

from Tkinter import*
import tkMessageBox
import os
#import subprocess

root=Tk()
root.title("Aryabhatt-A Basic Math Learning Software")
root.geometry("740x440")

#Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-Topic's",font=("Helvetica", 20),anchor=CENTER).grid(column=1,row=1,columnspan=7)

#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def ram():
     os.system("python quiz.py" )

def perido():
     os.system("python periodic.py" )
     
def about():
	'''
	Load the About Info Box.
	'''
        tkMessageBox.showinfo("About Aryabhatt!","Welcome to Aryabhatt! v0.1\n Aryabhatt is developed to explore Tkinter and then started off as a simple application.\nAryabhatt! is maintained at \nhttps://github.com/jervis/Aryabhatt/ \n\nYour contributions and suggestions are welcome. Feel free to fork and pull changes to Aryabhatt! The application is open-source and is open for development.\n\nAryabhatt is developed and maintained by Adarsh kumar. For suggestions and changes, feel free to drop an email:\n kumar[dot]adarshluv99[at]gmail[dot]com .\n\nInitial Release: Nov '17.")
   
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
button8.grid(column=1,row=0)
button8.config( height = 1, width = 2)
    
button1=Button(root,text="Trignometry",bg="blue",bd=5,fg="white",command=ram)
button1.grid(column=3,row=3)
button1.config( height = 10, width = 9)
button2=Button(root,text="Basic \nIntegration \nFormulae",bd=5,bg="pink",fg="blue",command=quit)
button2.grid(column=4,row=3)
button2.config( height = 10, width = 9)
button3=Button(root,text="Newton's \n Laws",bg="sky blue",bd=5,fg="white",command=ram)
button3.grid(column=3,row=4)
button3.config( height = 10, width = 9)
button4=Button(root,text="Modern \nPeriod \ntable",bd=5,bg="green",fg="blue",command=perido)
button4.grid(column=4,row=4)
button4.config( height = 10, width = 9)
button5=Button(root,text="Newton's \n Laws",bg="white",bd=5,fg="black",command=ram)
button5.grid(column=5,row=3)
button5.config( height = 10, width = 9)
button6=Button(root,text="Modern \nPeriod \ntable",bd=5,bg="light green",fg="white",command=quit)
button6.grid(column=5,row=4)
button6.config( height = 10, width = 9)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=1,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
