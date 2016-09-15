import soccer_club

url = "http://en.soccerwiki.org/"

players_data = {}               # Dictionary that holds entire player's data


for club_number in range(soccer_club.team_count):
    player_info = []            # List for player name
    player_temp_info = []       # List for player age and position
    player_count = 0            # Number of players in the club

    # Create soup object by appending url + club url from team_data list
    soup = soccer_club.make_soup(url + soccer_club.team_data[club_number]['club_url'])

    # Find div element with class name Innerborder that contains data can be webscraped
    links = soup.find_all("div", {"class": "InnerBorder"})

    # Find all player's name, split last and first names by comma, and rejoin them with first and last name as a string
    for link in links:
        for player_link in link.find_all('a'):
            players = player_link.get('href')
            if "player" in players:
                player_count += 1
                player_lists = player_link.text.split(',')
                player = ''.join(player_lists[1].lstrip().capitalize() + ' ' + player_lists[0].capitalize())
                player_info.append({'player_name': player})

        # Find player's age and position and then append to temporary list called player_temp_info
        for position_link in link.find_all("span", {"class": "actualPos"}):
            position = position_link.next_sibling.text
            age = position_link.next_sibling.parent.next_sibling.text
            player_temp_info.append({'age': age, 'position': position})

    # Merge all player's name, age and position to player_info list
    for count in range(player_count):
        player_info[count]['age'] = player_temp_info[count]['age']
        player_info[count]['position'] = player_temp_info[count]['position']

    # Define key value pairs and append the player_info to player key
    players_data = {
        'player': player_info
    }

    # Update the team_data list with players_data dictionary added
    soccer_club.team_data[club_number].update(players_data)

    # Find club's nickname and year found
    club_links = soup.find_all("div", {"class": "CRcontentBox floatright"})
    for club_link in club_links:
        nickname = club_link.find_all("td", {"class": "left"})[1].text
        year_found = club_link.find_all("td", {"class": "left"})[4].text

        # Append nickname and year_found to team_data list
        soccer_club.team_data[club_number]['nickname'] = nickname
        soccer_club.team_data[club_number]['year_found'] = year_found

print(soccer_club.team_data)