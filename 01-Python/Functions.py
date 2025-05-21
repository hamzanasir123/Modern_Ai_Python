# Functions

# Block Of Statements That Perform A Specific Task

def sum(a,b):
    print(a + b)


sum(2,3)

def printHello():
    print("Hello")

printHello()


# Average Of 3 Numbers

def avg(a,b,c):
    r = a + b + c
    res = r / 3
    print(res)
    return res

avg(23,45,56)


# Built-in Functions & User Defined Functions

# Built-in Functions

# print()
# len()
# type()
# range()

# User Defined Functions

# Default Perameters

def cal(a,b = 2) :
    print(a + b)

cal(2)   


# Practice Questions

Heroes = ["Iron Man", "Captain America" , "Hulk"]


def lenOfList(list) :
        print(len(list))


lenOfList(Heroes)

def printList(list) :
    print(list)

printList(Heroes)    

