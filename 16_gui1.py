from tkinter import * # access all the classes from tkinter module
import sys

root = Tk() # create a blank window

root.geometry("800x600") # set window size
root.configure(bg="white") # set window background color
root.attributes('-alpha', 0.9) # set window transparency
root.title("Tkinter GUI, bitch") # set window title

#Label
lblTitle = Label(root, text='Tkinter window label1, bitch') 
lblTitle.grid(column=1, row=0) 

lblTitle2 = Label(root, text='This is label 2')
lblTitle2.grid(column=1, row=1)

lblTitle3 = Label(root, text="Label 3 in center")
lblTitle3.place(anchor='center', relx=0.5, rely=0.5)

#Entry
entryName = Entry(root)
entryName.place(anchor='center', relx=.5, rely=.2)

#function gets text from entry and prints it out to the terminal and label
def print_name():
    print(entryName.get())
    lblTitle3.config(text=entryName.get()) # gets text entered in textbox and prints to label3
    
#Button
btnShowIt = Button(root, text='Print stuff form text box', width=20, command=print_name)
btnShowIt.place(anchor='center', relx=0.5, rely=0.7)

#bind window to key strokes 
def close_window(event): # event listener for keystrokes
    sys.exit() # once pressed, the window will close
    
root.bind('<Escape>', close_window) 

root.mainloop() # start main loop to show the form # keep the window open



