from abc import ABC
from dataclasses import dataclass
from datetime import date
from typing import Protocol


@dataclass(eq=True, frozen=True)
class Booking:
    client_id: int
    room_name: str
    arrival_date: date
    departure_date: date


@dataclass(eq=True, frozen=True)
class Room:
    room_name: str


class Repository(Protocol):
    def load_all(self) -> set[Room]:
        ...


class QueryService:
    def __init__(self, rooms=[], bookings=[], room_repository: Repository = None):
        if room_repository:
            self.rooms = room_repository.load_all()
        else:
            self.rooms = rooms
        self.bookings = bookings

    def free_rooms(self, arrival_date, departure_date):
        return {room for room in self.rooms if room.room_name not in self._unavailable_rooms()}

    def _unavailable_rooms(self):
        return {booking.room_name for booking in self.bookings}
