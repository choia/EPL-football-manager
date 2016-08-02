import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    soup_data = BeautifulSoup(r.content, "html.parser")
    return soup_data


soup = make_soup("http://en.soccerwiki.org/league.php?leagueid=28")

counts = 0
team_list = []
team = {}
team_data = []

for link in soup.find_all("td", {"class": "team left"}):
    link_text = link.get_text()
    if len(link_text) > 1:
        counts += 1
        team_list.append(link_text)


count = [x for x in range(counts) if x % 4 == 0]

for c in count:
    team = {team_list[c]: {'coach_name': team_list[c+1], 'stadium_name': team_list[c+2], 'city_name': team_list[c+3]}}
    team_data.append(team)

# print(team_data) FOR TESTING
# print(team_data[1]['Arsenal']['city_name']) FOR TESTING


