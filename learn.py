"""Aryabhatt - A Basic Math Learning Software """

from Tkinter import*
import tkMessageBox
import subprocess

root=Tk()
root.title("Aryabhatt-A Basic Math Learning Software")
root.geometry("670x340")

#Label(root,text="Welcome to",font=("Helvetica", 25)).grid(column=3,row=0,columnspan=3)
Label(root,text="Aryabhatt-A Basic Math Learning Software",font=("Helvetica", 20),anchor=CENTER).grid(column=1,row=0,columnspan=7)
createWidgets()

#Label(root,text="enter a number").grid(column=0,row=0,column span=4)

def ram():
     subprocess.call("python quiz.py" )
     
     
def quit():
	'''
	Function to confirm quit when the player presses Quit Button. If yes, Quit the application, If no, return to the game.
	'''
	choice = tkMessageBox.askyesno('Quit Application','Are you sure you wish to stop playing Aryabhatt! ?')
	if choice == True:
		root.destroy()
	elif choice == False:
		pass

def createWidgets():
	'''
	Function that creates all the necessary Tkinter widgets. All the widgets are specified here while creation.
	'''
	top = self.winfo_toplevel()
#	top.configure(background="white")

	#Creating the menu buttons
	self.menu = tk.Menu(self)
	self.menubar = tk.Menu(self.menu, tearoff=0)
	self.menubar.add_command(label="New Game", command=self.new_game)
	self.menubar.add_command(label="About", command=self.about)
	self.menubar.add_command(label="Quit", command=self.confirm_quit)
	top.config(menu=self.menubar)
    

    
button1=Button(root,text="LEARN",bd=5,fg="blue",command=ram)
button1.grid(column=3,row=3)
button1.config( height = 10, width = 7)
button2=Button(root,text="TRY",bd=5,fg="blue",command=quit)
button2.grid(column=4,row=3)
button2.config( height = 10, width = 7)
#Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)

bottomLabel = Label(root, text="Created by Adarsh kumar  (kumar.adarshluv99@gmail.com) under Prof. Mahesh sir [Dept. of CSE, JUET guna]")
bottomLabel.grid(column=0,row=12,columnspan=9)

"""akhiri shabd"""
root.mainloop()
root.destroy()
