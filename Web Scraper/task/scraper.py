import string
import requests
from http import HTTPStatus
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class ContentParser:
    def __init__(self):
        self.url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
        self.data_set = {}

    def data_parse(self, data_type):
        url = urlparse(self.url)
        response = requests.get(self.url)
        if response.status_code == HTTPStatus.OK:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article')
            for article in articles:
                article_type = article.find_next('span', {'class': "c-meta__type"})
                if article_type.text == data_type:
                    article_url = article.find_next('a', {'data-track-action': "view article"})
                    article_title = article_url.text.strip()
                    response_article = requests.get(f'{url.scheme}://{url.netloc}{article_url.get("href")}')
                    if response_article.status_code == HTTPStatus.OK:
                        soup_article = BeautifulSoup(response_article.content, 'html.parser')
                        article_body = soup_article.find('div', {'class': 'c-article-body'})
                        self.data_set[article_title] = article_body.text.strip()
                    else:
                        print(f'The URL returned {response_article.status_code}')
        else:
            print(f'The URL returned {response.status_code}')

    def data_save(self):
        for article_title, article_text in self.data_set.items():
            file = open(str_to_file_name(article_title), 'wb')
            file.write(bytes(article_text, 'utf-8'))
            file.close()


def str_to_file_name(s):
    return ''.join([ch for ch in s if ch not in string.punctuation]).replace(' ', '_') + '.txt'


def main():
    news_parser = ContentParser()
    news_parser.data_parse('News')
    news_parser.data_save()


if __name__ == '__main__':
    main()
