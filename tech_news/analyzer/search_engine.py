import datetime
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
    try:
        str_to_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        formated_date = str_to_date.strftime("%d/%m/%Y")
        # date_to_str = str(formated_date)
        query = ({"timestamp": formated_date})

        results = search_news(query)

        return [(
            result["title"],
            result["url"])
            for result in results
        ]
    except (ValueError, TypeError):
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
