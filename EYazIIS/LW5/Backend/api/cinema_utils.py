import logging

import requests
from bs4 import BeautifulSoup
import urllib.parse

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# todo find most related result from list using bs4
def get_search_result_url(query: str):
    return f'https://www.kinopoisk.ru/index.php?kp_query={query}'


# todo use kinopoisk
def get_image_url_by_query(query: str) -> str | None:
    return None

    encoded_query = urllib.parse.quote_plus(query)

    # Заголовки для имитации браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        url = f"https://www.google.com/search?q={encoded_query}&tbm=isch"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            logger.error(f"Can't get page: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        images = soup.find_all('img')

        image_urls = [img.get('src') for img in images if img.get('src') and len(img.get('src')) > 20]

        return image_urls[0] if image_urls else None

    except Exception as e:
        logger.error(f"{str(e)}")
        return None


if __name__ == '__main__':
    try:
        url = get_image_url_by_query("кошки")
        print(f"URL первой картинки: {url}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")