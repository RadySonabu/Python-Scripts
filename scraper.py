from bs4 import BeautifulSoup
import requests

source = requests.get('https://twitter.com/AUbanos').text
soup = BeautifulSoup(source, 'lxml')


# print(soup.prettify())

for post in soup.find_all('div', class_='js-tweet-text-container'):
	text = post.p.text
	print(text)
	
	print()


'''
	1. source = requests.get('<specific url or website you want to scrape>').text
	2. soup = BeautifulSoup(source, 'lxml')
	3. Using your web browser, right click and click inspect to a specific area you want to scrape the data.
	4. Find the div or tags you of the data you want to scrape.
	5. Find the class of the div you chose
	5. for post in soup.find_all('<specific tag like div, header>', class_='<specific class like js-tweet-text-container, container, etc>')
	6. text = post.p.text // look for the other tags inside before the text
	7. create a loop
	


'''