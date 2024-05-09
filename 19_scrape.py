from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"

page = urlopen(url) 

sup = BeautifulSoup(page, "html.parser") # convert raw html data into a readable format 

print(sup) # print the html data
#targeted search for table wit attribute class : key wikitables
the_table = sup.find('table', {'class' : {'wikitable'}}) # find the table with the class wikitable
# find the first occurence of <tobdy> tag
the_body = the_table.find('tbody') # find the body of the table

the_trs = the_body.find_all('tr') # find all the rows in the table

game_list = [] # create an empty list

for tr in the_trs:
    the_tds = tr.find_all('td') # find all the columns in the row
    td_list = [] # create an empty list
    for td in the_tds: # find all occurence of <sup> tag
        if td.find('sup'):
            the_sup = td.find('sup') 
            the_sup.decompose() # removes the tag from html, destroys it
        if td.find('a'):
            contents = td.find('a').contents[0] # get the contents of the <a> tag zero'th element (label of block)
            
        elif td.find('span'): # date of release
            contents = td.find('span').contents[0] 
        else:
            contents = td.contents[0] 
            
        contents = str(contents) # convert the contents to a string
        contents = contents.replace('\n', '')
        
        td_list.append(contents) # append the contents to the list
        
if len(td_list) > 0:
    game_list.append(td_list) # append the list to the game list
    
for game in game_list:
    for i, element in enumerate(game):
        if i < len(game) - 1:
            print(f"'{element}'", end=",") # print the index and the element
        else:
            print(f"'{element}'") # print the index and the element
        
            
            
