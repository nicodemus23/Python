from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"
page = urlopen(url)
sup = BeautifulSoup(page, "html.parser")

the_table = sup.find('table', {'class': {'wikitable'}})
the_body = the_table.find('tbody')
the_trs = the_body.find_all('tr')

game_list = []

for tr in the_trs:
    the_tds = tr.find_all('td')
    if len(the_tds) >= 6:
        td_list = []
        td_list.append(the_tds[0].find('a').text.strip())  # Game
        td_list.append(the_tds[1].text.strip())  # Platform
        
        release_date = the_tds[2].find('span') # Release Date
        if release_date:
            td_list.append(release_date.text.strip())  # Release Date
        else:
            td_list.append("N/A")  # Set release date as "N/A" if not available
        
        td_list.append(the_tds[3].text.strip())  # Developer
        td_list.append(the_tds[4].text.strip())  # Publisher
        td_list.append(the_tds[5].text.strip())  # Sales
        game_list.append(td_list)

for game in game_list:
    print(f"Game: {game[0]}")
    print(f"Platform: {game[1]}")
    print(f"Release Date: {game[2]}")
    print(f"Developer: {game[3]}")
    print(f"Publisher: {game[4]}")
    print(f"Sales: {game[5]}")
    print("---")