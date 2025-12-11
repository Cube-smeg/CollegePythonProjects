import os
from datetime import datetime

class HotelBookingSystem:
    def __init__(self):
        self.rooms = {i: None for i in range(1, 11)}  # Rooms 1 to 10, initially available (None means not booked)
        self.bookings_file = 'bookings.txt'

    def display_available_rooms(self):
        """Display rooms that are available."""
        available_rooms = [room for room, booking in self.rooms.items() if booking is None]
        if available_rooms:
            print(f"Available rooms: {', '.join(map(str, available_rooms))}")
        else:
            print("No rooms available at the moment.")
        return available_rooms

    def is_valid_date(self, date_str):
        """Check if the input date is in the correct format and valid."""
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj
        except ValueError:
            return None

    def book_room(self, room_number, booking_date):
        """Book a room for a given date."""
        if room_number not in self.rooms:
            print("Invalid room number. Please select a room between 1 and 10.")
            return False

        if self.rooms[room_number] is not None:
            print(f"Room {room_number} is already booked on {self.rooms[room_number]}.")
            return False

        # If room is available, book it
        self.rooms[room_number] = booking_date
        self.save_booking_to_file(room_number, booking_date)
        print(f"Room {room_number} successfully booked for {booking_date}!")
        return True

    def save_booking_to_file(self, room_number, booking_date):
        """Save the booking information to a TXT file."""
        with open(self.bookings_file, 'a') as file:
            file.write(f"Room {room_number} booked on {booking_date}\n")

    def get_user_input(self):
        """Handle the user input for booking process."""
        # Get available rooms
        available_rooms = self.display_available_rooms()
        if not available_rooms:
            return

        # Get room choice
        try:
            room_number = int(input(f"Enter the room number you want to book (1-10): "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")
            return

        if room_number not in available_rooms:
            print(f"Room {room_number} is not available.")
            return

        # Get booking date
        booking_date_str = input("Enter the date of booking (YYYY-MM-DD): ")
        booking_date = self.is_valid_date(booking_date_str)
        if not booking_date:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Attempt to book the room
        self.book_room(room_number, booking_date_str)

# Main Program
def main():
    hotel_system = HotelBookingSystem()

    while True:
        print("\n--- Hotel Booking System ---")
        hotel_system.get_user_input()

        cont = input("Do you want to make another booking? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
