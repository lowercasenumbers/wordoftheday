import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.merriam-webster.com/word-of-the-day')
soup = BeautifulSoup(r.content, 'html.parser')

title_elm = soup.find('title')
title = title_elm.text

word = title.split()[4]
wodDefContainer = soup.find('div', class_='wod-definition-container')

definition_elm = wodDefContainer.find('p')
definition = definition_elm.text

attributes = soup.find('div' , class_='word-attributes')
main_attr = attributes.find('span', class_='main-attr').text
syllables = attributes.find('span', class_='word-syllables').text
examples = soup.find('div', class_='wotd-examples').text

print('Word of the Day:\n' + word + ' (' + main_attr + ' | ' + syllables + ' ) ' + definition + '\n' + examples)


