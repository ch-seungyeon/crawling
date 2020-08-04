import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv

URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')


movie_selection = soup.select(
'div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')

movie_list = []

for movie in movie_selection:
    a_tag = movie.select_one('dl>dt>a')
    movie_title = a_tag.text
    movie_code= a_tag['href']
    movie_code= movie_code.split('?code=')[1]

    movie_data = {
        "title" : movie_title,
        "code" : movie_code
    }
    
    movie_list.append(movie_data)
    # with open('./naver_movie.csv', 'a', encoding='utf-8-sig', newline='') as csvfile:
    #     fieldnames = ['title', 'code']
    #     csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #     csvwriter.writerow(news_data)
print(movie_list)