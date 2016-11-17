import soccer_club

url = "http://en.soccerwiki.org/"
players_data = {}                   # Dictionary that holds entire player's data

# Looping entire EPL team
for club_ID in range(soccer_club.team_count):

    player_info = {}                # Dictionary for player data
    player_count = 0                # Number of players in the club
    count = 0                       # Counter used to append age and position to player_info

    # Create soup object by appending url + club url from team_data list
    soup = soccer_club.make_soup(url + soccer_club.team_data[club_ID]['club_url'])

    # Find div element with class name Innerborder that contains data can be webscraped
    links = soup.find_all("div", {"class": "InnerBorder"})

    # Find all player's name, split last and first names by comma, and rejoin them with first and last name as a string
    for link in links:
        for player_link in link.find_all('a'):
            players = player_link.get('href')
            if "player" in players:
                player_lists = player_link.text.split(',')
                player = ''.join(player_lists[1].lstrip().capitalize() + ' ' + player_lists[0].capitalize())
                player_name = player_count
                player_info.update({player_name: [player]})
                player_count += 1

        # Find player's age and position and then append to player_info dictionary
        for position_link in link.find_all("span", {"class": "actualPos"}):
            position = position_link.next_sibling.text
            age = position_link.next_sibling.parent.next_sibling.text
            player_info[count].append(age)
            player_info[count].append(position)
            count += 1

    # Define key value pairs and append the player_info to player key
    players_data = {
        'players': player_info
    }

    # Update the team_data list with players_data dictionary added
    soccer_club.team_data[club_ID].update(players_data)

    # Find club's nickname and year found
    club_links = soup.find_all("div", {"class": "CRcontentBox floatright"})
    for club_link in club_links:
        nickname = club_link.find_all("td", {"class": "left"})[1].text
        year_found = club_link.find_all("td", {"class": "left"})[4].text

        # Append nickname and year_found to team_data list
        soccer_club.team_data[club_ID]['nick_name'] = nickname
        soccer_club.team_data[club_ID]['year_found'] = year_found

#print(soccer_club.team_data) # TEST
#print(players_data) # TEST
