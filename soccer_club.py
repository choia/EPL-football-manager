import requests
from bs4 import BeautifulSoup


# Define a function and use BeautifulSoup & Requests to webscrape data from specific url
def make_soup(url):
    r = requests.get(url)
    soup_data = BeautifulSoup(r.content, "html.parser")
    return soup_data


link_count = 0          # Count total number of texts that was parsed from the team left class
team_count = 0          # Count total number of clubs when adding data to the team data list
team_info_list = []     # List with club name, manager, stadium, and location
team_url_list = []      # List with club url
team_logo_list = []     # List with logo url
team_data = []          # Final list with all of appended club data

soup = make_soup("http://en.soccerwiki.org/league.php?leagueid=28")


# Find all the texts in team left class, append club name, manager name, stadium, and city to the team info list
for link in soup.find_all("td", {"class": "team left"}):
    link_text = link.get_text()
    if len(link_text) > 1:
        link_count += 1
        team_info_list.append(link_text)

    # Find all of team logo url(jpg) and append to the team logo list
    for jpg_link in link.find_all('img'):
        team_logo_list.append('http:' + jpg_link['src'])

    # Find all of club urls and append to the team url list
    for url_link in link.find_all('a'):
        urls = url_link.get('href')
        if "squad" in urls:
            team_url_list.append(urls)


# Calculate number of teams by link count(total number of texts) divided by 4;
# 4 being club name, manager, stadium and city
number_of_teams = [x for x in range(link_count) if x % 4 == 0]
# print(len(number_of_teams)) # FOR TEST - Print Number of EPL Teams

# Append all of items to the team data list
for club_data in number_of_teams:
    team_info = {
            'team_name': team_info_list[club_data],
            'manager': team_info_list[club_data + 1],
            'stadium': team_info_list[club_data + 2],
            'location': team_info_list[club_data + 3],
            'club_url': team_url_list[team_count],
            'logo_url': team_logo_list[team_count]
    }
    team_count += 1
    team_data.append(team_info)



#print(team_data)