import requests
import csv
from io import StringIO
from bs4 import BeautifulSoup

def scrapeSchedule():
    """Scrapes schedule from team pages."""

    payload_array = [['day', 'date', 'year', 'time', 'home', 'homeID', 'home_score', 'away', 'awayID', 'away_score', 'field']]

    # GET TEAMS LIST
    url = 'http://events.gotsport.com/events/schedule.aspx?eventid=67315&FieldID=0&applicationID=4788436&action=Go'
    #requests
    url_r = requests.get(url)
    #run the requests through soup
    url_soup = BeautifulSoup(url_r.content, "html.parser")

    try: 
        scheduleDiv = url_soup.find("div",{"class":"grid_12"})
        scheduleTables = scheduleDiv.findAll("table")

        for game in scheduleTables:
            game_rows = game.findAll("tr")
            
            date_list = game_rows[0].text.split(', ')
            game_day = date_list[0].lstrip()
            game_date = date_list[1]
            game_year = date_list[2]

            game_time = game_rows[2].find('div', {'class': 'MatchTime'}).text.replace('\xa0', '')
            
            home_team = game_rows[2].find('td', {'class': 'homeTeam'}).text
            away_team = game_rows[2].find('td', {'class': 'awayTeam'}).text

            home_id = game_rows[2].find('td', {'class': 'homeTeam'}).find('a')['href'].split("applicationID=")[1].split("&")[0]
            away_id = game_rows[2].find('td', {'class': 'awayTeam'}).find('a')['href'].split("applicationID=")[1].split("&")[0]

            scores = game_rows[2].findAll('span', {'class': 'score'})
            home_score = scores[0].text
            away_score = scores[1].text

            field = game_rows[2].find('td', {'class': 'location'}).findAll('div')[0].text

            payload_array.append([game_day, game_date, game_year, game_time, home_team, home_id, home_score, away_team, away_id, away_score, field])
    
        si = StringIO()
        cw = csv.writer(si)
        for row in payload_array:
            cw.writerow(row)

        # DEPLOY
        schedule_data = si.getvalue()
        return schedule_data
            
    except:
        print('Something broke')

# this function is just for our testing purposes,
# just calling the main handler function
if __name__ == '__main__':
    scrapeSchedule()