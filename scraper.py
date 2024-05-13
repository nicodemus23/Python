
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class NeumontScraper:
    def __init__(self, url): # https://www.knowledgehut.com/blog/programming/self-in-python (use of self in python)
        self.url = url
        request = Request(self.url)
        self.page = urlopen(request) 
        self.sup = BeautifulSoup(self.page, "html.parser")  # Convert raw HTML data into a readable format
        
    def scrape(self):
        calendar = self.sup.find('table')
        
        rows = calendar.find_all('tr')
        
        calendar_data = []
        
        # Iterate over each row
        for row in rows:
            # Check if the row is a heading row
            heading = row.find('th')
            if heading:
                # Extract the heading text and add it to the calendar data
                heading_text = heading.text.strip() # strip() removes leading and trailing whitespaces # https://www.programiz.com/python-programming/methods/string/strip
                calendar_data.append(("Heading", heading_text))
            else:
                # Find all the cells in the row
                cells = row.find_all('td')

                # Extract the date and event from the cells
                date = cells[0].text.strip()
                event = cells[1].text.strip()

                # Append the date and event as a tuple to the calendar_data list
                calendar_data.append((date, event))

        return calendar_data
        
