#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def book(self):
        self.is_available = False

    def checkout(self):
        self.is_available = True


class Guest:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        for room in self.rooms:
            status = "Available" if room.is_available else "Booked"
            print(f"Room {room.room_number} ({room.room_type}): {status} - Price: ${room.price}")

    def book_room(self, room_number, guest):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_available:
                    room.book()
                    self.guests.append(guest)
                    print(f"Room {room_number} booked for {guest.name}.")
                else:
                    print(f"Room {room_number} is already booked.")
                return
        print(f"Room {room_number} not found.")

    def checkout_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_available:
                    room.checkout()
                    print(f"Checked out from room {room_number}.")
                else:
                    print(f"Room {room_number} is already available.")
                return
        print(f"Room {room_number} not found.")


def main():
    hotel = Hotel()
    
    # Adding some rooms
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 250))
    
    while True:
        print("\n1. Show Rooms")
        print("2. Book Room")
        print("3. Checkout Room")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            hotel.show_rooms()
        elif choice == '2':
            name = input("Enter guest name: ")
            id_number = input("Enter guest ID number: ")
            guest = Guest(name, id_number)
            room_number = int(input("Enter room number to book: "))
            hotel.book_room(room_number, guest)
        elif choice == '3':
            room_number = int(input("Enter room number to checkout: "))
            hotel.checkout_room(room_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




