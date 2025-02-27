#...I. Data Abstraction
#...Exercise 01 : Airplane Ticket Booking System

# from abc import ABC, abstractmethod
# class airplaneTicket(ABC):
#     def __init__(self, passenger_name, ticket_price):
#         self.passenger_name = passenger_name
#         self.ticket_price = ticket_price

#     def book_ticket(self):
#         return f"Ticket booked for {self.passenger_name} - Price: ${self.ticket_price}"

#     @abstractmethod
#     def cancel_ticket(self):
#         pass

#     @abstractmethod
#     def display_ticket_info(self):
#         pass
# class Economy_Ticket(airplaneTicket):
#     def cancel_ticket(self):
#         return f"Ticket canceld for {self.passenger_name}. Refund Amount: ${self.ticket_price - (self.ticket_price * 0.5)}"
#     def display_ticket_info(self):
#         return f"Passenger: {self.passenger_name}, Ticket Price: ${self.ticket_price}, Type: Economy Class"

# class Business_Ticket(airplaneTicket):
#     def cancel_ticket(self):
#         return f"Ticket canceld for {self.passenger_name}. Refund Amount: ${self.ticket_price - (self.ticket_price * 0.3)}"
#     def display_ticket_info(self):
#         return f"Passenger: {self.passenger_name}, Ticket Price: ${self.ticket_price}, Type: Business Class"

# class First_Class(airplaneTicket):
#     def cancel_ticket(self):
#         return f"Ticket canceld for {self.passenger_name}. Refund Amount: ${self.ticket_price - (self.ticket_price * 0.1)}"
#     def display_ticket_info(self):
#         return f"Passenger: {self.passenger_name}, Ticket Price: ${self.ticket_price}, Type: First Class"
# Economy = Economy_Ticket("Visa", 500)
# print("Case Study 1:")
# print(Economy.book_ticket())
# print(Economy.display_ticket_info())
# print(Economy.cancel_ticket())
# print("\n")
# Business = Business_Ticket("Rio", 1000)
# print("Case Study 2:")
# print(Business.book_ticket())
# print(Business.display_ticket_info())
# print(Business.cancel_ticket())
# print("\n")
# First = First_Class("Alice", 2000)
# print("Case Study 3:")
# print(First.book_ticket())
# print(First.display_ticket_info())
# print(First.cancel_ticket())

#...Exercise 02: Library Management System

from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, book_name, magazine_name):
    def borrow_book(self, book_name):
    