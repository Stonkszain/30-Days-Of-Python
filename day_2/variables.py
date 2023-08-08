# Day 2: 30 Days of python programming
import math

first_name = 'Zain'
last_name = 'Safdar'
full_name = 'Zain Safdar'
country = 'Wonderland'
city = 'Moon'
age = 20.0
year = 2003
is_married = False
is_true = True
is_light_on = False
happy, sad, excited = True, False, "Ofcourse"

print(type(full_name),type(age),type(year))

if len(first_name) > len(last_name):
    print(f'{first_name} is longer than {last_name}')
elif len(first_name) < len(last_name):
    print(f'{last_name} is longer than {first_name}')
else:
    print(f'Both names are equal')

num_one, num_two = 5,4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30 # User input
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print(f'Area: {area_of_circle}')
print(f'Circumference: {circum_of_circle}')

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
country = input("Enter Country: ")
city = input("Enter City: ")
age = int(input("Enter Age: "))
year = int(input("Enter Year: "))

help('keywords')