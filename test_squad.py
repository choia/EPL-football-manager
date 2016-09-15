import sys
import soccer_club

url = "http://en.soccerwiki.org/"


# Create soup object by appending url + club url from team_data list
soup = soccer_club.make_soup(url + soccer_club.team_data[0]['club_url'])

link1 = soup.find_all("div", {"class": "CRcontentBox floatright"})
for link2 in link1:
    print(link2.find_all("td", {"class": "left"})[1].text)
    print(link2.find_all("td", {"class": "left"})[4].text)