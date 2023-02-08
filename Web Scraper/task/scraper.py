import requests
from http import HTTPStatus
from bs4 import BeautifulSoup
from urllib.parse import urlparse


MSG = {
    'error_status_code': 'Invalid quote resource!'
}

CONTENT_KEY = 'content'


def main():
    url_input = input('Input the URL:')
    # url_input = 'https://www.nature.com/articles/d41586-023-00103-3'
    url = urlparse(url_input)
    response = requests.get(url_input)
    if response.status_code == HTTPStatus.OK:
        file = open('source.html', 'wb')
        page_content = response.content
        file.write(page_content)
        file.close()
        print('Content saved.')
    else:
        print(f'The URL returned {response.status_code}')


if __name__ == '__main__':
    main()
