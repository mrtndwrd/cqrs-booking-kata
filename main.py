from dataclasses import dataclass
from datetime import date


@dataclass(eq=True, frozen=True)
class Booking:
    client_id: int
    room_name: str
    arrival_date: date
    departure_date: date


@dataclass(eq=True, frozen=True)
class Room:
    room_name: str


class QueryService:
    def __init__(self, rooms=[], bookings=[]):
        self.rooms = rooms
        self.bookings = bookings

    def unbooked_room_generator(self):
        for room in self.rooms:
            for booking in self.bookings:
                if booking.room_name != room.room_name:
                    yield room

    def free_rooms(self, arrival_date, departure_date):
        if self.bookings:
            return set(self.unbooked_room_generator())
        return set(self.rooms)
