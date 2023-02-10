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
        html_content = response.text

        if response.status_code != 200:
            return None

    except (ReadTimeout):
        return None

    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()
    return html_content


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()

    url_list = []

    for post in soup.find_all(
        "article", {"class": "entry-preview"}
    ):
        url_list.append(post.find(
            "div",
            {"class": "cs-overlay"},
        ).a["href"])
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()

    if html_content:
        return soup.find(
                "div",
                {"class": "nav-links"}
        ).find(
            "a",
            {"class": "next"},
        )["href"]

    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
