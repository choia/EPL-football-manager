from xml.dom import minidom
from collections import OrderedDict

doc = minidom.parse('c:\\PythonGit\staging\soccer_club\clubdata.xml')

club_lists = OrderedDict()

clubs = doc.getElementsByTagName('C')
for club in clubs:
    #print(club.getAttribute('id'), club.getAttribute('n'))
    club_id = club.getAttribute('id')
    club_team = club.getAttribute('n')
    club_lists[club_id] = club_team

#for club in club_lists:
#    print(club, club_lists[club])

# Outputting Club ID and Club to clubs.txt file
filename = 'clubs.txt'
with open(filename, 'w', encoding='utf-8') as filename_object:
    for club in club_lists:
        filename_object.write(club)
        filename_object.write('\t')
        filename_object.write(club_lists[club])
        filename_object.write('\n')