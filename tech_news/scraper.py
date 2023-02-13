from bs4 import BeautifulSoup
import requests
from requests.exceptions import ReadTimeout
import time
import re
from .database import create_news


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
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()

    news = {}

    news["url"] = soup.find(
        "div", {"class": "pk-share-buttons-wrap"}
    )["data-share-url"]

    news["title"] = soup.find(
        "h1", {"class": "entry-title"}
    ).string.replace("\xa0", " ").strip()

    news["timestamp"] = soup.find("li", {"class": "meta-date"}).string

    news["writer"] = soup.find(
        "span", {"class": "author"}
    ).string

    news["reading_time"] = int(re.sub('[^0-9]', '', soup.find(
        "li", {"class": "meta-reading-time"}
    ).text))

    news["summary"] = soup.find(
        "div", {"class": "entry-content"}
    ).p.text.replace("\xa0", " ").strip()

    news["category"] = soup.find("span", {"class": "label"}).text

    return news


# Requisito 5
def get_tech_news(amount):
    scraped_news = []
    url = "https://blog.betrybe.com"
    url_news_list = []

    while len(url_news_list) <= amount:
        html_content = fetch(url)

        url_news_list.extend(scrape_updates(html_content))

        if scrape_next_page_link(html_content) is not None:
            url = scrape_next_page_link(html_content)

    for each_url in url_news_list[:amount]:
        each_html_content = fetch(each_url)
        data_news = scrape_news(each_html_content)

        scraped_news.append(data_news)

    create_news(scraped_news)
    return scraped_news
