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
    def display_details(self):
        print(f"Name of the Movie: {self.title}")
        print(f"Theater: {self.theater.name} ({self.theater.city})")
        print(f"Language of the Movie: {self.language}")
        print(f"IMDb Rating: {self.imdb_rating}")
        print(f"Genre: {self.genre}")
        print(f"Cast: {', '.join(self.cast)}")
        print(f"Crew: {', '.join(self.crew)}")
        print(f"Cost of each ticket: {self.cost}")
        print(f"Date: {self.date}")
        print(f"Day: {self.day}")
        print(f"Show Timing: {self.timing}")
        print(f"Available Seats: {self.seats}")
        
class Theater:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class CinemaConnect:
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
                print(f"{i+1}. {city}")

    def display_movies(self, city):
        available_movies = [movie for movie in self.movies if movie.theater.city == city]
        if len(available_movies) == 0:
            print("No movies available for the selected city.")
        else:
            for i, movie in enumerate(available_movies):
                print("Showing Movies for today:")
                print(f"{i + 1}. {movie.title} ({movie.timing}) - {movie.theater.name}")
                print(f"{movie.language}, {movie.genre}, {movie.imdb_rating}/10")
                print(f"{movie.cast}")
                print(f"{movie.crew}")
                print(f"   ")

    def book_ticket(self, city, movie_index, num_tickets, row, seat):
     available_movies = [movie for movie in self.movies if movie.theater.city == city]
     if len(available_movies) == 0:
        print("No movies available for the selected city.")
        return
     elif movie_index < 1 or movie_index > len(available_movies):
        print("Invalid movie index.")
        return
    
     movie = available_movies[movie_index - 1]
     movie.display_seat_map()  # Display seat map here
    
     if num_tickets > movie.seats:
        print("Not enough seats available.")
        return

     selected_seats = []
     for i in range(num_tickets):
        if not (0 <= row[i] < 20 and 0 <= seat[i] < 25):
            print("Seat Selection Error. Please try again.")
            return
        if not movie.is_seat_available(row[i], seat[i]):
            print("Selected seat is already booked. Please select another seat.")
            return
        selected_seats.append((row[i], seat[i]))


     customer_name = input("Enter the customer name: ")
     mobile_number = input("Enter the mobile number: ")
     email = input("Enter the email: ")

     total_cost = num_tickets * movie.cost
     print("Seats:")
     for seat in selected_seats:
          print(f"Row: {seat[0]}, Seat: {seat[1]}")
     print(f"Total Cost: INR {total_cost} only")
      
     for seat in selected_seats:
          movie.book_seat(seat[0], seat[1], customer_name)

     print("\nPayment Options:")
     print("1. Credit Card")
     print("2. Debit Card")
     print("3. Paytm")

     payment_option = int(input("Select a payment option: "))

     self.process_payment(payment_option, total_cost, movie, customer_name, email, mobile_number)
            
    def display_bookings(self, city, movie_index):
        filtered_movies = [movie for movie in self.movies if movie.theater.city == city]
        if len(filtered_movies) == 0:
            print("No movies available for the selected city.")
            return
        if movie_index < 1 or movie_index > len(filtered_movies):
            print("Invalid movie number.")
            return
        movie = filtered_movies[movie_index - 1]
        print(f"Bookings for {movie.title} ({movie.timing}) - {movie.theater.name} ({movie.theater.city}):")
        movie.display_seat_map()
    @staticmethod
    def validate_mobile_number(self, mobile_number):
        pattern = r"^[6-9]\d{9}$"
        return re.match(pattern, mobile_number) is not None
    @staticmethod
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return re.match(pattern, email) is not None

    def process_payment(self, payment_option, total_cost, movie, customer_name, email, mobile_number):

        if payment_option == 1: # Credit Card
            credit_card_number = input("Enter your credit card number: ")
            name_on_card = input("Enter the name on the card: ")
            expiry_date = input("Enter expiry date (MM/YY): ")
            cvv = input("Enter the CVV: ")
            if len(credit_card_number) != 16 or not re.match(r"^\d+$", credit_card_number):
                print("Invalid credit card number. Please enter a valid 16-digit card number.")
                return

            if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", expiry_date):
                print("Invalid expiry date. Please enter a valid date in MM/YY format.")
                return

            if len(cvv) != 3 or not re.match(r"^\d+$", cvv):
                print("Invalid CVV. Please enter a valid 3-digit CVV.")
                return

            print("Processing credit card payment...(3)")
            time.sleep(1)
            print("Processing credit card payment...(2)")
            time.sleep(1)
            print("Processing credit card payment...(1)")
        # Add payment gateway integration logic here
            print(f"Payment of INR {total_cost} processed successfully.")

            print("\nReceipt:")
            movie.display_details()
            print(f"Movie: {movie.title}")
            print(f"Theater: {movie.theater.name} ({movie.theater.city})")
            print(f"Date: {movie.date}")
            print(f"Day: {movie.day}")
            print(f"Timing: {movie.timing}")
            print(f"Name of the Customer: {customer_name}")
            print(f"Mobile Number of the Customer: {mobile_number}")
            print(f"Email address of the Customer : {email}")

        elif payment_option == 2:  # Debit Card
            debit_card_number = input("Enter debit card number: ")
            expiry_date = input("Enter expiry date (MM/YY): ")
            cvv = input("Enter CVV: ")

            if len(debit_card_number) != 16 or not re.match(r"^\d+$", debit_card_number):
                print("Invalid debit card number. Please enter a valid 16-digit card number.")
                return

            if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", expiry_date):
                print("Invalid expiry date. Please enter a valid date in MM/YY format.")
                return

            if len(cvv) != 3 or not re.match(r"^\d+$", cvv):
                print("Invalid CVV. Please enter a valid 3-digit CVV.")
                return

            print("Processing debit card payment...(3)")
            time.sleep(1)
            print("Processing debit card payment...(2)")
            time.sleep(1)
            print("Processing debit card payment...(1)")
        # Add payment gateway integration logic here
            print(f"Payment of INR {total_cost} processed successfully.")

            print("\nReceipt:")
            movie.display_details()
            print(f"Movie: {movie.title}")
            print(f"Theater: {movie.theater.name} ({movie.theater.city})")
            print(f"Date: {movie.date}")
            print(f"Day: {movie.day}")
            print(f"Timing: {movie.timing}")
            print(f"Name of the Customer: {customer_name}")
            print(f"Mobile Number of the Customer: {mobile_number}")
            print(f"Email address of the Customer : {email}")
            # Process debit card details
          
        elif payment_option == 3:
            paytm_number = input("Enter your Paytm mobile number: ")
            OTP = input("Enter the 6-digit OTP: ")
            if not re.match(r"^[6-9]\d{9}$", paytm_number):
                print("Invalid UPI mobile number. Please enter a valid UPI mobile number.")
                return

            if len(OTP) != 6 or not re.match(r"^\d+$", OTP):
                print("Invalid OTP. Please check again.")
                return

            print("Processing debit card payment...(3)")
            time.sleep(1)
            print("Processing debit card payment...(2)")
            time.sleep(1)
            print("Processing debit card payment...(1)")
            # Add payment gateway integration logic here
            print(f"Payment of INR {total_cost} processed successfully.")

            print("\nReceipt:")
            movie.display_details()
            print(f"Movie: {movie.title}")
            print(f"Theater: {movie.theater.name} ({movie.theater.city})")
            print(f"Date: {movie.date}")
            print(f"Day: {movie.day}")
            print(f"Timing: {movie.timing}")
            print(f"Name of the Customer: {customer_name}")
            print(f"Mobile Number of the Customer: {mobile_number}")
            print(f"Email address of the Customer : {email}")

        else:         
            print("Invalid payment option. Please select a valid payment option.")
            return
    
   

