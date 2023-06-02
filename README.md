# project.py

import re
import time


class Movie:
    def __init__(self, title, timing, theater, rows, seats_per_row, cost, genre, imdb_rating, language, cast, crew, is_3d=False, has_dolby=False, date=None, day=None):
        self.title = title
        self.timing = timing
        self.theater = theater
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.total_seats = rows * seats_per_row
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
        self.seat_map = {}


    def is_seat_available(self, seat):
        return self.seat_map.get(seat) is None

    def book_seat(self, seat, customer_name):
        self.seat_map[seat] = customer_name

    def display_seat_map(self):
       for row in range(1, self.rows + 1):
         row_letter = chr(64 + row)  # Convert row number to letter (A=1, B=2, etc.)
         seats = [f"{row_letter}{seat}" for seat in range(1, self.seats_per_row + 1) if self.is_seat_available(f"{row_letter}{seat}")]
         
         print(f"Row {row_letter}: {', '.join(seats)}")



    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Timing: {self.timing}")
        print(f"Theater: {self.theater.name} ({self.theater.city})")
        print(f"Genre: {self.genre}")
        print(f"IMDb Rating: {self.imdb_rating}")
        print(f"Language: {self.language}")
        print(f"Cast: {', '.join(self.cast)}")
        print(f"Crew: {', '.join(self.crew)}")
        print(f"Cost: {self.cost}")
        print(f"Date: {self.date}")
        print(f"Day: {self.day}")
        print(f"Available Seats: {self.total_seats - len(self.seat_map)}")


class Theater:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class BookMyShow:
    def __init__(self):
        self.cities = []
        self.movies = []

    def add_city(self, city):
        self.cities.append(city)

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_cities(self):
        if len(self.cities) == 0:
            print("No cities available.")
        else:
            print("Cities available:")
            for i, city in enumerate(self.cities):
                print(f"{i+1001}. {city}")

    def display_movies(self, city):
        filtered_movies = [movie for movie in self.movies if movie.theater.city == city]
        if len(filtered_movies) == 0:
            print("No movies available for the selected city.")
        else:
            print("Movies available:")
            for i, movie in enumerate(filtered_movies):
                print(f"{i+1}. {movie.title} ({movie.timing}) - {movie.theater.name}")

    def book_ticket(self, city, movie_index, num_tickets):
      filtered_movies = [movie for movie in self.movies if movie.theater.city == city]
      if len(filtered_movies) == 0:
        print("No movies available for the selected city.")
        return
      if movie_index < 1 or movie_index > len(filtered_movies):
         print("Invalid movie index.")
         return
      movie = filtered_movies[movie_index - 1]
      if num_tickets > (movie.total_seats - len(movie.seat_map)):
        print("Not enough seats available.")
      else:
        print("Seat Map:")
        movie.display_seat_map()

        print("Please select seats (row and seat number such as A2 or D5).")
        selected_seats = []
        while len(selected_seats) < num_tickets:
            seat_input = input(f"Select seat {len(selected_seats) + 1}: ")
            if not re.match(r"[A-Z]\d+", seat_input):
                print("Invalid seat selection. Please try again.")
                continue

            if not self.is_valid_seat(movie, seat_input):
                print("Selected seat is already booked or invalid. Please select another seat.")
                continue

            selected_seats.append(seat_input)
            movie.book_seat(seat_input, None)

        customer_name = input("Enter your name: ")
        mobile_number = input("Enter your 10-digit mobile number: ")

        # Validate mobile number
        if not self.validate_mobile_number(mobile_number):
            print("Invalid mobile number. Please enter a 10-digit number.")
            return

        email = input("Enter your email address: ")

        # Validate email address
        if not self.validate_email(email):
            print("Invalid email address. Please enter a valid email.")
            return

        total_cost = num_tickets * movie.cost

        # Choose payment method
        print("\nPayment Options:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Paytm")

        payment_option = int(input("Select a payment option: "))

        # Process payment
        self.process_payment(payment_option, total_cost)

        # Print receipt
        print("\nReceipt:")
        movie.display_details()
        print(f"Customer: {customer_name}")
        print(f"Mobile Number: {mobile_number}")
        print(f"Email: {email}")
        print("Seats:")
        for seat in selected_seats:
            print(f"Seat: {seat}")
        print(f"Total Cost: {total_cost}")

        # Mark booked seats as unavailable
        for seat in selected_seats:
            movie.seat_map[seat] = customer_name

        # Prompt to book again
        book_again = input("Do you want to book tickets again? (yes/no): ")
        if book_again.lower() == "yes":
            num_seats_again = int(input("Enter the number of seats to book again: "))
            self.book_ticket(city, movie_index, num_seats_again)



    def display_bookings(self, city, movie_index):
        filtered_movies = [movie for movie in self.movies if movie.theater.city == city]
        if len(filtered_movies) == 0:
            print("No movies available for the selected city.")
            return
        if movie_index < 1 or movie_index > len(filtered_movies):
            print("Invalid movie index.")
            return
        movie = filtered_movies[movie_index - 1]
        print(f"Bookings for {movie.title} ({movie.timing}) - {movie.theater.name} ({movie.theater.city}):")
        movie.display_seat_map()

    def process_payment(self, payment_option, total_cost):
        if payment_option == 1: # Credit Card
            account_number = input("Enter your account number: ")
            name_on_card = input("Enter the name on the card: ")
            cvv = input("Enter the CVV: ")
            print("Processing credit card payment...(3)")
            time.sleep(1)
            print("Processing credit card payment...(2)")
            time.sleep(1)
            print("Processing credit card payment...(1)")
        # Add payment gateway integration logic here
            print(f"Payment of INR {total_cost} processed successfully.")


        elif payment_option == 2:  # Debit Card
            account_number = input("Enter your account number: ")
            name_on_card = input("Enter the name on the card: ")
            cvv = input("Enter the CVV: ")
            print("Processing debit card payment...(3)")
            time.sleep(1)
            print("Processing debit card payment...(2)")
            time.sleep(1)
            print("Processing debit card payment...(1)")
        # Add payment gateway integration logic here
            print(f"Payment of INR {total_cost} processed successfully.")

            # Process debit card details
          
        elif payment_option == 3:  # UPI
            valid_upi_pattern = r"^[a-zA-Z0-9]+(?:/[0-9]+)?(?:/[a-zA-Z0-9]+)?@[ybioaxl]{3}$"
            upi_id = input("Enter your UPI ID: ")

            if not re.match(valid_upi_pattern, upi_id):
                print("Invalid UPI ID. Please enter a valid UPI ID in the specified format.")
                # Handle invalid UPI ID case
            else:
                # Process UPI details
                 print("Processing UPI payment...(3)")
                 time.sleep(1)
                 print("Processing UPI payment...(2)")
                 time.sleep(1)
                 print("Processing UPI payment...(1)")
        # Add payment gateway integration logic here
                 print(f"Payment of INR {total_cost} processed successfully.")
 
        elif payment_option == 4:  # Paytm
            valid_mobile_number_pattern = r"^[6-9][0-9]{9}$"
            mobile_number = input("Enter your Paytm mobile number: ")

            if not re.match(valid_mobile_number_pattern, mobile_number):
                print("Invalid Paytm mobile number. Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9.")
                # Handle invalid mobile number case
            else:
                # Process Paytm details
                 print("Processing Paytm payment...(3)")
                 time.sleep(1)
                 print("Processing Paytm payment...(2)")
                 time.sleep(1)
                 print("Processing Paytm payment...(1)")
        # Add payment gateway integration logic here
                 print(f"Payment of INR {total_cost} processed successfully.")
                 
        else:
            print("Invalid Paytm number")

    @staticmethod
    def validate_mobile_number(mobile_number):
        pattern = r"^[6-9]\d{9}$"
        return re.match(pattern, mobile_number) is not None

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) 

    @staticmethod
    def is_valid_seat(movie, seat):
        row = int(seat[1:])
        seat_character = seat[0]

        if not seat_character.isalpha() or row > movie.rows or ord(seat_character.upper()) - 65 + 1 > movie.seats_per_row or ord(seat_character.upper()) - 65 + 1 < 1:
            return False

        if seat in movie.seat_map:
            return False

        return True



# Example usage

bms = BookMyShow()

# Adding cities
bms.add_city("Mumbai")
bms.add_city("Delhi")
bms.add_city("Bangalore")
bms.add_city("Palakkad")

# Adding movies
theater1 = Theater("Cineplex", "Mumbai")
theater2 = Theater("PVR Cinemas", "Delhi")
theater3 = Theater("INOX MOVIES", "Banglore")
movie1 = Movie("Avengers: Endgame", "9:00 AM", theater1, 5, 10, 100, "Action", 8.5, "English", ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"], ["Anthony Russo", "Joe Russo"], is_3d=True, has_dolby=True, date="2023-05-30", day="Monday")
movie2 = Movie("The Lion King", "2:00 PM", theater2, 5, 8, 50, "Animation", 7.9, "English", ["Donald Glover", "Beyoncé", "Chiwetel Ejiofor"], ["Jon Favreau"], is_3d=False, has_dolby=False, date="2023-05-30", day="Monday")
bms.add_movie(movie1)
bms.add_movie(movie2)

# Displaying available cities
bms.display_cities()

# Displaying movies in a city
city_index = int(input("Enter the city index to browse movies: "))
bms.display_movies(bms.cities[city_index - 1001])

# Booking tickets
movie_index = int(input("Enter the movie index to book tickets: "))
num_tickets = int(input("Enter the number of tickets: "))
bms.book_ticket(bms.cities[city_index - 1001], movie_index, num_tickets)

# Displaying bookings for a movie in a city
city_index = int(input("Enter the city index to view bookings: "))
movie_index = int(input("Enter the the movie index to view bookings: "))
bms.display_bookings(bms.cities[city_index - 1001], movie_index)
