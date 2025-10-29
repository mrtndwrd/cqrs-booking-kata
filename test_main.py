from datetime import date
from main import QueryService


def test_free_rooms_returns_empty_set_when_there_are_no_rooms():
    query_service = QueryService()
    result = query_service.free_rooms(arrival_date=date(
        2023, 1, 1), departure_date=date(2023, 1, 2))
    assert result == set()
