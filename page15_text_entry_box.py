from tkinter import*
import tkinter as tk
root=None
entryBox=None 
def button_pushed():
  global entryBox
  txt=entryBox.get()
  print("The text is %s "%(txt))
def createBox(Parent):
	global entryBox
	entryBox=Entry(Parent) 
	entryBox.pack()   
def main():
	 global root
	 root = Tk() 
	 myButton=Button(root, text="Show Text",command=button_pushed)
	 myButton.pack()
	 createBox(root)
	 root.geometry("300x300")
	 root.mainloop()
    
     
     

main()


