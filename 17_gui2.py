# using TK with canvas layout
# this will give a nice organization to the window and allow
# to place controls on the canvas

from tkinter import * # access all the classes from tkinter module
import sys # import the sys module for system functions 
import tkinter.font as tkFont # import the font module from tkinter

root = Tk() # create a blank window
root.geometry("800x600") # set window size
root.configure(bg="white") # set window background color

#bind window to key strokes 
def close_window(event): # event listener for keystrokes
    sys.exit() # once pressed, the window will close
    
root.bind('<Escape>', close_window) 

#Layout 
canvas_header = Canvas(root, height=50) # create a canvas
canvas_header.pack(side='top', fill=BOTH) # pack the canvas to the top of the window
canvas_header.configure(bg='gray') # set canvas background color

canvas_footer = Canvas(root, height=50) # create a canvas
canvas_footer.pack(side='bottom', fill=BOTH) # pack the canvas to the top of the window
canvas_footer.configure(bg='darkgray') # set canvas background color

canvas_left = Canvas(root, height=200) # create a canvas
canvas_left.pack(side='left', fill=BOTH) # pack the canvas to the top of the window
canvas_left.configure(bg='blue') # set canvas background color

canvas_right = Canvas(root, height=100) # create a canvas
canvas_right.pack(side='right', fill=BOTH) # pack the canvas to the top of the window
canvas_right.configure(bg='red') # set canvas background color

#Font styles
font_title = tkFont.Font(family='Arial 16 bold', size=20)
font_page = tkFont.Font(family='Arial 16 bold', size=12)

#Controls
lblTitle = Label(canvas_header, text='Welcome, yall!', font=font_title, fg='white', bg='red')
lblTitle.place(relx=.5, rely=.5, anchor='center')  

lblName = Label(canvas_left, text="What's your name?", font=font_page, fg='orange', bg='blue')
lblName.grid(column=0, row=0, padx=10, pady=10)

entryName = Entry(canvas_left)
entryName.grid(column=0, row=1, padx=20)

counter_names = 0 # counter for names / global variable

def post_name(event): # event listener for keystrokes
    global counter_names # global variable
    counter_names += 1 # increment counter (have to specify an index for the list box)
    txtName.insert(END, entryName.get() + '\n') # insert text from entry box to text box / end means the end of the text widget
    lbName.insert(counter_names, entryName.get()) # insert text from entry box to list box
    #lbName.insert(END, entryName.get()) # insert text from entry box to list box
    entryName.delete(0, 'end') # clear the entry box 
    

#entryName = Entry(canvas_left) # create an entry box
#entryName.grid(column=0, row=1, padx=20) # place the entry box on the canvas
entryName.bind('<Return>', post_name) # bind the enter key to the post_name function

txtName = Text(canvas_left, font=font_page, height=5, bg='lightblue', width=20) # multi-line text box
txtName.grid(column=0, row=4, padx=20, pady=10)

lbName = Listbox(canvas_footer, font=font_page, width=25, bg='lightgreen') # list box
#lbName.place(anchor='center', relx=.5, rely=.1)
lbName.pack(anchor='center', padx=2, pady=2)

# canvas colors: https://www.tkinter.org/doc/stable/reference/colors.html

root.mainloop() # start main loop to show the form # keep the window open