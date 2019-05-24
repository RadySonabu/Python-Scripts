from bs4 import BeautifulSoup
import requests

source = requests.get('https://twitter.com/AUbanos').text
soup = BeautifulSoup(source, 'lxml')


# print(soup.prettify())

for post in soup.find_all('div', class_='js-tweet-text-container'):
	text = post.p.text
	print(text)
	print()