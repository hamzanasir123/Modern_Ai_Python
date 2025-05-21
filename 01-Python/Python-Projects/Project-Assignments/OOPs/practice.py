# 1. Class aur Static Variables
# Task:
# Ek Library class banao jo books ka record rakhti hai. Isme ek class variable total_books ho jo
# saari libraries ke liye shared ho. Har library ka instance apna name aur book_list rakhe. Ek
# method add_book banao jo book add kare aur total_books ko update kare. Ek method
# show_books banao jo library ke books aur total books dikhaye.
# Test: 2 libraries banao, dono mein books add karo, aur check karo ke total_books sahi update
# hota hai ya nahi.
# Focus: Class vs instance variables, accessing/modifying class variables.

class Library:
    total_books = 0
    def __init__(self,name,book_list=[]):
        self.name = name
        self.book_list = book_list

    def add_book(self,book):
        self.total_books += 1
        self.book_list += book

    def show_books(self):
        print("Library Books = ", self.book_list)
        print("Total Books = ", self.total_books)

library1 = Library("King")
library1.add_book("Hamza Nasir")
library1.add_book(" Shah Rukh Khan")
library1.show_books()

print(library1.total_books)



# 2. Composition aur Aggregation
# Task:
# Ek House class banao jo rooms ko store kare. Room class alag se banao jisme room_type (e.g.,
# "Bedroom") aur area ho. House mein rooms list ke zariye aggregation use karo. Ek method
# add_room banao jo naye rooms add kare, aur total_area method jo saare rooms ka area calculate
# kare.
# Test: Ek house banao, 3 rooms add karo, aur total area print karo.
# Focus: Aggregation, has-a relationship.

class Room:
    def __init__(self,room_type,area):
        self.room_type = room_type
        self.area = area


class House:
    def __init__(self):
        self.rooms = []

    def add_room(self,room):
        self.rooms.append(room)

    def total_area(self):
        return sum(room.area for room in self.rooms)
    

house = House()
house.add_room(Room("BedRoom", 120))
house.add_room(Room("LivingRoom", 130))
house.add_room(Room("Master BedRoom", 220))

print("Total area of the house:", house.total_area(), "sq ft")


# 3. Method Resolution Order (MRO)
# Task:
# Teen classes banao: Parent, Child1, aur Child2. Parent mein ek introduce method ho jo "I am
# Parent" return kare. Child1 aur Child2 is method ko override karen aur apna message return
# karen. Ek GrandChild class banao jo Child1 aur Child2 dono se inherit kare. introduce call karo
# aur MRO print karo.
# Test: GrandChild ka object banao, introduce call karo, aur mro() method se order check karo.
# Focus: Multiple inheritance, MRO understanding.



class Parent:
    def introduce(self):
        return "I Am Parent."

class Child1(Parent):
    def introduce(self):
        return "I Am Child1"

class Child2(Parent):
    def introduce(self):
        return "I Am Child2"


class GrandChild(Child1,Child2):
    pass


gc = GrandChild()

print(gc.introduce())
print(GrandChild.mro())


# 4. Decorators in Classes
# Task:
# Ek Employee class banao jisme salary attribute ho. @property use karke salary ka getter banao.
# @salary.setter se salary update karne ka method banao jo check kare ke salary positive hai. Ek
# computed property bonus banao jo salary ka 10% return kare.
# Test: Employee banao, salary set karo, bonus check karo, aur negative salary set karne ki
# koshish karo.
# Focus: Property decorators, getter/setter, computed properties



class Employee:
    def __init__(self,salary):
        self._salary = None
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary Must Be Positive")
        self._salary = value

    @property
    def bonus(self):
        return self.salary * 0.10
    

em1 = Employee(50000)
print(em1.salary)
print(em1.bonus)

em1.salary = 100000
print(em1.salary)
print(em1.bonus)


