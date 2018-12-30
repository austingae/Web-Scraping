from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.youtube.com/feed/trending").text
# print(source)

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

section = soup.find('ol', class_ = "section-list")
print(section.prettify())

# title = section.find('div', class_= "yt-lockup-content").h3.a.text
# print(title)

# id="item-section-783571" class="item-section"
# ol id="section-list-567838" class="section-list"
# "yt-lockup-content"