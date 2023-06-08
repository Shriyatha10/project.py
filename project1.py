import re
import time

class Movie:
    def __init__(self, title, timing, theater, seats, cost, genre, imdb_rating, language, cast, crew, is_3d=False, has_dolby=False, date=None, day=None):
        self.title = title
        self.timing = timing
        self.theater = theater
        self.seats = seats
        self.cost = cost
        self.genre = genre
        self.imdb_rating = imdb_rating
        self.language = language
        self.cast = cast
        self.crew = crew
        self.is_3d = is_3d
        self.has_dolby = has_dolby
        self.date = date
        self.day = day
        self.seat_map = [[None] * 25 for _ in range(20)]  # Seat map for a theater with 20 rows and 25 seats per row

    def is_seat_available(self, row, seat):
        return self.seat_map[row][seat] is None

    def book_seat(self, row, seat, customer_name):
        self.seat_map[row][seat] = customer_name
        self.seats -= 1

    def display_seat_map(self):
        print("Seat Map:")
        for row in self.seat_map:
            for seat in row:
                if seat is None:
                    print("⬜", end=" ")
                else:
                    print("🟨", end=" ")
            print()
