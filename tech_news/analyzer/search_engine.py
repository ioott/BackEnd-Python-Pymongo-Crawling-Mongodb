import re
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    query = ({"title": {"$regex": regex}})
    results = search_news(query)

    return [(
        result["title"],
        result["url"])
        for result in results
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
