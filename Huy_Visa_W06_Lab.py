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

# from abc import ABC, abstractmethod
# class LibraryItem(ABC):

#     @abstractmethod
#     def borrow(self):
#         pass
#     @abstractmethod
#     def returnn(self):
#         pass
    
#     def duration(self, day):
#         x1 = int(0)
#         x2 = int(14)
#         if day < x1:
#             return "Invalid date"
#         elif day > x2:
#             return "You can only borrow the book for 14 days"
#         return f"You have {day} days to return the book."

# class Books(LibraryItem):
#     bookList = [
#         "1984",
#         "To kill the mockingbird",
#         "Sapien's: A Brief History of humankind",
#         "The Alchemist",
#         "The Hobbit",
#         "The Catcher in the Rye",
#         "Atomic Habits",
#         "The Subtle Art of not Giving a Fu*k",
#         "Dune",
#         "Pride and Prejudice"
#     ]
#     def borrow(self):
#         borrow = input("Enter the book title: ")
#         Book_duration = input("How long will you return the book (1-14) Day?:")
#         time = int(Book_duration)
#         if time > 14 or time <= 0:
#             print("Invalid Date")
#         elif borrow in self.bookList:
#             print(f"{borrow} is successfully borrow!")
#         else:
#             print("Book not Available")
#         print(self.duration(time))

#     def returnn(self):
#         bookTitle = input("What book you want to return: ")
#         dateToreturn = input("How many day have you been borrow the book?: ")
#         intofdate = int(dateToreturn)
#         if bookTitle in self.bookList:
#             print(f"{bookTitle} have return successfully!")
#         if intofdate > 14 or intofdate <= 0:
#             print("You get 20$ penalty!")
#         else: 
#             print("See you next time!")
    
#     def searchBook(self):
#         print("Book list:\n")
#         for x in self.bookList:
#             print(f"{x}")
        
# class Magazines(LibraryItem):
#     magazineList = [
#         "Tech Trend Weekly",
#         "Innovate Today",
#         "The Science Digest",
#         "Creative Minds",
#         "Future Finance",
#         "Health & Wellness Monthly",
#         "Traveller Paradise"
#     ]
#     def borrow(self):
#         borrow = input("Enter the magazine title: ")
#         Magazine_duration = input("How long will you return the magazine (1-14) Day?")
#         time = int(Magazine_duration)
#         if time > 14 or time <= 0:
#             print("Invalid Date")
#         elif borrow in self.magazineList:
#             print(f"{borrow} is successfully borrow!")
#         else:
#             print("Magazine not Available")
#         print(self.duration(time))

#     def returnn(self):
#         bookTitle = input("What book you want to return: ")
#         dateToreturn = input("How many day have you been borrow the book?: ")
#         intofdate = int(dateToreturn)
#         if bookTitle in self.magazineList:
#             print(f"{bookTitle} have return successfully!")
#         if intofdate > 14 or intofdate <= 0:
#             print("You get 10$ penalty!")
#         else: 
#             print("See you next time!")
    
#     def searchMagazine(self):
#         print("Magazine list:\n")
#         for x in self.magazineList:
#             print(f"{x}")
# #>>>Main<<<#
# #...Book
# # Book1 = Books()

# # Book1.borrow()
# # Book1.returnn()
# # Book1.searchBook()

# #...Magazine
# Magazine1 = Magazines()

# Magazine1.borrow()
# Magazine1.returnn()
# Magazine1.searchMagazine()