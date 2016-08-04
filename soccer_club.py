import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    soup_data = BeautifulSoup(r.content, "html.parser")
    return soup_data


soup = make_soup("http://en.soccerwiki.org/league.php?leagueid=28")

count = 0
team_count = 0
team_data = []
team_list = []

team_url_list = []
team_logo_list = []

for link in soup.find_all("td", {"class": "team left"}):
    link_text = link.get_text()
    if len(link_text) > 1:
        count += 1
        team_list.append(link_text)

    for src in link.find_all('img'):
        # print(src['src']) # FOR TESTING
        team_logo_list.append(src['src'])

    for a_data in link.find_all('a'):
        urls = a_data.get('href')
        if "squad" in urls:
            # print(urls) # FOR TESTING
            team_url_list.append(urls)

# print(team_logo_list) # FOR TESTING
# print(team_url_list) # FOR TESTING
# print(team_list) # FOR TESTING

number_of_teams = [x for x in range(count) if x % 4 == 0]
# print(len(number_of_teams)) # FOR TESTING

for club_data in number_of_teams:
    team_info = {
        team_list[club_data]: {
            'coach_name': team_list[club_data + 1],
            'stadium_name': team_list[club_data + 2],
            'city_name': team_list[club_data + 3],
            'club_url': team_url_list[team_count],
            'logo_url': team_logo_list[team_count]
        }
    }
    team_count += 1
    print(team_info)
    team_data.append(team_info)

# print(team_data) # FOR TESTING
# print(team_data[1]['Arsenal']['city_name']) # FOR TESTING





