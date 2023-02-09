from bs4 import BeautifulSoup
import requests
from requests.exceptions import ReadTimeout
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        html_page = response.text

        if response.status_code != 200:
            return None

    except (ReadTimeout):
        return None

    soup = BeautifulSoup(html_page, "html.parser")
    soup.prettify()
    return html_page


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
