root=None
entryBox=None , a global reference  for the root window and for the  entry box 
------------------------------------------------------------------------------
def button_pushed(): ,begining of the button_pushed method 
  global entryBox
  txt=entryBox.get() ,assigment of the text which  the user will enter in the entry  box to the variable txt   by calling   the get() operation  to get it when we push the button 
  print("The text is %s "%(txt))  ,the command  which prints on the screen the text entered 
  ---------------------------------------------------------------------------------------------- 
  def createBox(Parent):
	global entryBox
	entryBox=Entry(Parent) ,creation of the entry box 
	entryBox.pack()      , placement of the entry box within the main window 
   ----------------------------------------------------------------------------------------------
   def main():
	 global root
	 root = Tk()  ,creation of the main window of our app 
	 myButton=Button(root, text="Show Text",command=button_pushed)  ,creation of our button 
	 myButton.pack() ,placement of the button within our main window 
	 createBox(root) ,call of the function  createBox(root
	 root.geometry("300x300") ,size definition of our window 
	 root.mainloop() ,start the app 
  ------------------------------- 
  main() call the main function  

 You can find the code in   Tkinter – GUIs in Python  Dan Fleck CS112 George Mason University
https://cs.gmu.edu/~dfleck/classes/cs112/spring08/slides/tkinter.pdf

