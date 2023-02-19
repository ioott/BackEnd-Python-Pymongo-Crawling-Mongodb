from tech_news.database import find_news, get_collection


# Requisito 10
def top_5_categories():
    all_news = get_collection()
    top_categories = all_news.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5}
    ])
    top_categories = [category['_id'] for category in top_categories]

    if len(top_categories) < 5:
        all_categories = {news['category'] for news in find_news()}
        remaining_categories = sorted(all_categories - set(top_categories))
        top_categories += remaining_categories[:5 - len(top_categories)]

    return top_categories
