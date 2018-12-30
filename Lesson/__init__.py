from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.khanacademy.org").text
# print(source)

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('li', class_ = "subjectListItem_wgzm6k"):
    # print(article.prettify())

    headline = article.a.text
    print(headline)

# for article in soup.find_all('ul', class_ = "domainContents_u0ffi4"):
#     subjects = article
#     print(subjects.prettify())


# soup = BeautifulSoup(source,'lxml')
# csv_file = open('csm_scrape.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])
# for article in soup.find_all('article'):
#     # print(article.prettify())
#
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.find('div', class_ = 'entry-content').p.text
#     print(summary)
#
#     video_source = article.find('iframe',class_ = 'youtube-player')['src']
#     print(video_source)
#
#     video_id = video_source.split('/')[4].split('?')[0]
#     print(video_id)
#
#     youtube_link = f'https://www.youtube.com/?v={video_id}'
#     print(youtube_link)
#
#     print()
#
#     csv_writer.writerow([headline, summary, youtube_link])
#
# csv_file.close()
#
#
# Tasks:
# 1. Get all Youtube titles in trending section
#

