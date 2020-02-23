from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    headline  = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content').p.text
    print (summary)

    try:
        yt_link = article.find('iframe',class_='youtube-player')['src']
        yt_link = yt_link.split('/')
        yt_link = yt_link[4]
        yt_link = yt_link.split('?')
        yt_link = yt_link[0]
        print (f'www.youtube.com/watch?v={yt_link}')

    except:
        print ("link not found")
    print ("\n")
