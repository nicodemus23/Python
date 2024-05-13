import tkinter as tk
from tkinter import * # access all the classes from tkinter module
import tkinter.font as tkFont # import the font module from tkinter
from scraper import NeumontScraper
import sys

root = Tk() # create a blank window
root.geometry("800x600") # set window size
root.configure(bg="white") # set window background color

def close_window(event): # event listener for keystrokes
    sys.exit() # once pressed, the window will close
    
root.bind('<Escape>', close_window)

#Layout
canvas_header = Canvas(root, height=50) # create a canvas
canvas_header.pack(side='top', fill=BOTH) # pack the canvas to the top of the window
canvas_header.configure(bg='gray') # set canvas background color

canvas_content = Canvas(root) # create a canvas
canvas_content.pack(fill=BOTH, expand=True) # pack the canvas to the top of the window
canvas_content.configure(bg='white') # set canvas background color

#Font styles
#Font styles
font_title = tkFont.Font(family='Arial 16 bold', size=20)
font_page = tkFont.Font(family='Arial 16 bold', size=12)

#Controls
lblTitle = Label(canvas_header, text='Neumont Academic Calendar Scraper', font=font_title, fg='white', bg='gray')
lblTitle.place(relx=.5, rely=.5, anchor='center')

def scrape():
    url = "https://neumont.smartcatalogiq.com/en/2023-2024/catalog/academic-calendar-2023-2024/spring-quarter-2024/"
    scraper = NeumontScraper(url)
    calendar_data = scraper.scrape()
        
    output_text.delete(1.0, tk.END) # Clear the output text area
        
        # Display the scraped data in the scrollable area
    for element in calendar_data:
        if element[0] == "Heading":
            output_text.insert(tk.END, f"Heading: {element[1]}\n")
        else:
            date, event = element
            output_text.insert(tk.END, f"Date: {date}\nEvent: {event}\n\n") 
            
            # output_text.insert(tk.END, f"Quarter: {item['quarter']}\n")
            # output_text.insert(tk.END, f"Date: {item['date']}\n")
            # output_text.insert(tk.END, f"Event: {item['event']}\n\n")
        
def save():
    with open("neumont_calendar.txt", "w") as file:
        file.write(output_text.get(1.0, tk.END))
        
scrape_button = Button(canvas_content, text="Scrape Calendar", font=font_page, command=scrape)
scrape_button.pack(pady=10)

save_button = Button(canvas_content, text="Save to File", font=font_page, command=save)
save_button.pack(pady=5)

output_text = Text(canvas_content, font=font_page, height=20, width=80)
output_text.pack(padx=20, pady=10)

scrollbar = Scrollbar(canvas_content) # create a scrollbar
scrollbar.pack(side=RIGHT, fill=Y) # pack the scrollbar to the right of the window
output_text.config(yscrollcommand=scrollbar.set) # set the text widget to scroll
scrollbar.config(command=output_text.yview) # set the scrollbar to scroll the text widget

root.mainloop() # run the window
        

# Create an appealing GUI interface using any Python library. The GUI should contain the following:
# A Title and description for this application
# A button that when clicked will scrape the website
# (optional) A button that when clicked will save the scraped data to a file
# A scrollable area to display the output
# Use Beautiful Soup to obtain the headings, dates, and events from the current catalog
# Print the data in the scrollable area in the GUI and make it easily readable.  Show the date and events.
# Use a class in your code somehow
# Import a module of yours, from a separate file


# Submission Requirements:

# Submit the python scripts you wrote
# Pass off in person, or video of it running, with code and full explanations

# This criterion is linked to a Learning OutcomeUse Beautiful Soup to obtain the quarter headings, dates, and events from the current catalog

# This criterion is linked to a Learning OutcomePrint the data on the screen so that it is easily readable

# This criterion is linked to a Learning OutcomeImport your own module py file that does the scraping

# This criterion is linked to a Learning OutcomeUse a class
