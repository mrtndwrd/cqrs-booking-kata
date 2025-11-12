from datetime import date
from main import Booking, QueryService, Room

arrival_date = date(2023, 1, 1)
departure_date = date(2023, 1, 2)


class RoomRepository:
    def __init__(self, rooms):
        self._rooms = rooms

    def load_all(self):
        return self._rooms.copy()


def test_free_rooms_returns_empty_set_when_there_are_no_rooms():
    query_service = QueryService(room_repository=RoomRepository(rooms=[]))
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == set()


def test_free_rooms_returns_a_room_when_there_are_no_bookings():
    rooms = [Room(room_name="101")]
    room_repo = RoomRepository(rooms)
    query_service = QueryService(
        bookings=[], room_repository=room_repo)
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="101")}


def test_free_rooms_returns_no_room_if_there_is_a_booking_for_it():
    rooms=[Room(room_name="101")]
    room_repo = RoomRepository(rooms)
    query_service = QueryService(
        room_repository=room_repo,
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == set()


def test_free_rooms_returns_only_the_rooms_that_have_no_bookings():
    rooms=[Room(room_name="101"), Room(room_name="102")]
    room_repo = RoomRepository(rooms)
    query_service = QueryService(
        room_repository=room_repo,
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="102")}


def test_free_rooms_returns_only_the_rooms_that_have_no_bookings():
    rooms=[Room(room_name="101"), Room(
        room_name="102"), Room(room_name="103")]
    room_repo = RoomRepository(rooms)
    query_service = QueryService(
        room_repository=room_repo,
        bookings=[Booking(client_id=1, room_name="101",
                          arrival_date=arrival_date, departure_date=departure_date)],
    )
    result = query_service.free_rooms(
        arrival_date=arrival_date, departure_date=departure_date)
    assert result == {Room(room_name="102"), Room(room_name="103")}

def test_free_rooms_after_new_room_is_added_to_repository(): 
    room_repo = RoomRepository([])
    service = QueryService(
        room_repository=room_repo,
        bookings=[],
    )
    new_room = Room(room_name="new")
    room_repo._rooms.append(new_room)

    free_room = service.free_rooms(arrival_date=arrival_date, departure_date=departure_date)
    assert free_room == {new_room}


