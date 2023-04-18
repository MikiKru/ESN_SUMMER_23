# CTRL + / - comment
# CTRL + D - duplicate cursor line
import random
from math import sqrt

name = 'Michal'
number = random.randint(2, 5)
print(name)
print("My name is: " + name)
print("My final grade is: " + str(number))
print("My final grade is:", number, sep=';')
print("My final grade is:", number, sep=';', end='\n')  # \n newline
print("My final grade is:", number, sep=';', end='')
print("My final grade is:", number, sep=';', end='')
print("My final grade is:", number, sep=';', end='')
print("My final grade is:", number, sep=';')

print(type(name))
print(type(number))

num1_str = '123'
num1_int = int(num1_str)

print(type(num1_str), 'is convert to',type(num1_int))

print("I\'m John. My favourite sentence is : \"...\"")


_temp_value = 1
color = 'Blue'
COLOUR = 'Red'
# 4you ... you can not start from digit
you4 = '...'    # it's ok
# you_four - snake case -> youFour - camel style
print(color == COLOUR)
this_is_variable = "XYZ"

# 2^3
print(2**3)
# 3^3
print(3**3, pow(3,3), sqrt(9))

print(3 >= 2)
print("Alice" > "Alan")

# data_from_user = input("write sth...")
# print(data_from_user)

try:
    user_grade = int(input("write number from following interval [2-5]"))
    print(user_grade)
except ValueError:
    print("your value is not integer!")