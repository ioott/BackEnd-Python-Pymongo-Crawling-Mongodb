from tech_news.analyzer.reading_plan import ReadingPlanService
from pytest import raises
from unittest.mock import patch

mock_input = [
    {"title": "Noticia Mock 01", "reading_time": 8},
    {"title": "Noticia Mock 02", "reading_time": 7},
    {"title": "Noticia Mock 03", "reading_time": 20},
    {"title": "Noticia Mock 04", "reading_time": 15},
]

mock_read = [
    {"chosen_news": [("Noticia Mock 01", 8)], "unfilled_time": 2},
    {"chosen_news": [("Noticia Mock 02", 7)], "unfilled_time": 3},
]

mock_unread = [('Noticia Mock 03', 20), ('Noticia Mock 04', 15)]


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock_input
    ):
        news = ReadingPlanService.group_news_for_available_time(10)
        assert news["readable"] == mock_read
        assert news["unreadable"] == mock_unread
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        news = ReadingPlanService.group_news_for_available_time(0)
