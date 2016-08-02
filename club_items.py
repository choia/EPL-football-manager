import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    soup_data = BeautifulSoup(r.content, "html.parser")
    return soup_data


soup = make_soup("http://en.soccerwiki.org/league.php?leagueid=28")


number_of_teams = 20
team_url_list = []
team_logo_list = []

for link in soup.find_all('td', {'class': 'team left'}):
    # print(link) # FOR TESTING
    for src in link.find_all('img'):
        # print(src['src']) # FOR TESTING
        team_logo_list.append(src['src'])

    for a_data in link.find_all('a'):
        urls = a_data.get('href')
        if "squad" in urls:
            # print(urls) # FOR TESTING
            team_url_list.append(urls)


print(team_logo_list)
print(team_url_list)