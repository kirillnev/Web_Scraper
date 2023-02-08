import requests
from http import HTTPStatus
from bs4 import BeautifulSoup
from urllib.parse import urlparse


MSG = {
    'error_status_code': 'Invalid quote resource!'
}

CONTENT_KEY = 'content'


def main():
    url_input = input()
    # url_input = 'https://www.nature.com/articles/d41586-023-00103-3'
    url = urlparse(url_input)
    if url.netloc == 'www.nature.com' and url.path.split('/')[1] == 'articles':
        response = requests.get(url_input)
        if response.status_code == HTTPStatus.OK:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title')
            description = soup.find('meta', {'name': 'description'})
            result = {'title': title.text, 'description': description.get('content')}
            print(result)
        else:
            print('Invalid page!')
    else:
        print('Invalid page!')


if __name__ == '__main__':
    main()
