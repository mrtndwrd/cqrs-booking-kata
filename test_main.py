from datetime import date
from main import Booking, QueryService, Room

arrival_date = date(2023, 1, 1)
departure_date = date(2023, 1, 2)


def test_free_rooms_returns_empty_set_when_there_are_no_rooms():
    query_service = QueryService()
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == set()


def test_free_rooms_returns_a_room_when_there_are_no_bookings():
    query_service = QueryService(rooms=[Room(room_name="101")], bookings=[])
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="101")}


def test_free_rooms_returns_no_room_if_there_is_a_booking_for_it():
    query_service = QueryService(
        rooms=[Room(room_name="101")],
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == set()


def test_free_rooms_returns_only_the_rooms_that_have_no_bookings():
    query_service = QueryService(
        rooms=[Room(room_name="101"), Room(room_name="102")],
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="102")}


def test_free_rooms_returns_only_the_rooms_that_have_no_bookings():
    query_service = QueryService(
        rooms=[Room(room_name="101"), Room(
            room_name="102"), Room(room_name="103")],
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="102"), Room(room_name="103")}
