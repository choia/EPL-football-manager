import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    soup_data = BeautifulSoup(r.content, "html.parser")
    return soup_data


soup = make_soup("http://en.soccerwiki.org/league.php?leagueid=28")

counts = 0
team_list = []
team_data = []

for link in soup.find_all("td", {"class": "team left"}):
    link_text = link.get_text()
    if len(link_text) > 1:
        counts += 1
        team_list.append(link_text)

# print(team_list) # FOR TESTING

number_of_teams = [x for x in range(counts) if x % 4 == 0]
# print(len(number_of_teams)) # FOR TESTING

for club_data in number_of_teams:
    team_info = {
        team_list[club_data]: {
            'coach_name': team_list[club_data + 1],
            'stadium_name': team_list[club_data + 2],
            'city_name': team_list[club_data + 3]}
    }

    team_data.append(team_info)

print(team_data) # FOR TESTING
# print(team_data[1]['Arsenal']['city_name']) # FOR TESTING


