# Simple web crawler with Beautiful Soup
from bs4 import BeautifulSoup
import requests


def simple_crawler():
    """"
    # Remember to have an url with complete access.
    # request it
    # use html parser to interpret as html.
    """
    url = ''
    html_url = requests.get(url)
    soup = BeautifulSoup(html_url.content, 'html.parser')

    # Texts, with the following html tag.
    texts = soup.findAll('p', )

    # Store text on a list.
    several_texts = []
    list_numbers = 1

    # print all texts.
    for one_text in texts:
        several_texts.append(one_text.text) # .text is to only extract raw text and no html tags.
        list_numbers += 1
        # print(list_numbers, several_texts)

    return list(several_texts)


raw_text = simple_crawler()

for text in raw_text:
    print(text)

