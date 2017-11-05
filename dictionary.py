from bs4 import BeautifulSoup
import bs4
import re
from urllib.request import urlopen
word = input("Search word: ")
try:
    html = urlopen("https://en.oxforddictionaries.com/definition/"+word)
    soup = BeautifulSoup(html, "html5lib")
    variant = soup.find('div', attrs= {'class':'variant'})
    print('ALSO: \n')
    for child in variant.findChildren():
        print(child.text)
    print('\nPRONOUNCIATION\n')
    prons = soup.find('div', attrs={'class': 'pron'}).findChildren()
    for pron in prons:
        print(pron.text)
    print('\nMEANINGS\n')
    
    sections = soup.find_all('section', attrs={'class': 'gramb'})
    for section in sections:
        print(section.find('span', attrs={'class': 'pos'}).text)
        meanings = section.find('ul', attrs={'class': 'semb'}).find_all('span')
        examples = section.find('ul', attrs={'class': 'semb'}).find_all('em')
        for meaning in meanings:
            if re.search("[0-9]",meaning.text):
                print('\n')
                print(meaning.text)
            else:
                print(meaning.text)
        print('\nEXAMPLES:\n')
        for example in examples[:3]:
            print(example.text)
        print('\n\n')
    print('\nORIGINS\n')
    print(soup.find('div', attrs={'class':'senseInnerWrapper'}).find('p').text)
    
except:
    print('NOT FOUND')
