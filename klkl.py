from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')
# print (soup.prettify())
article = soup.find('article')
headline = article.h2.a.text
