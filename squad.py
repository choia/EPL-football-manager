from bs4 import BeautifulSoup
import requests

url = 'http://en.soccerwiki.org/squad.php?clubid=1'
page = requests.get(url)

soup = BeautifulSoup(page.content)
print(soup)