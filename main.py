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


class RoomRepository(Protocol):
    def load_all(self) -> set[Room]:
        ...

class BookingRepository(Protocol):
    def load_all(self) -> list[Booking]:
        ...


class QueryService:
    def __init__(self, booking_repository: BookingRepository, room_repository: RoomRepository = None):
        self.room_repository = room_repository
        self.bookings = booking_repository.load_all()

    def free_rooms(self, arrival_date, departure_date):
        all_rooms = self.room_repository.load_all()
        return {room for room in all_rooms if room.room_name not in self._unavailable_rooms()}

    def _unavailable_rooms(self):
        return {booking.room_name for booking in self.bookings}
