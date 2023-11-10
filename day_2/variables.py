# Day 2: 30 Days of Python Programming
import math

first_name = 'Devontae'
last_name = 'Hudson'
full_name = first_name + last_name
country = 'Canada'
city = 'Toronto'
age = 23
year = 2023
is_married = False
is_true = True
is_light_on = True
school, degree, likes_programming = 'Western University', 'Mechatronic Systems Engineering', True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(school))
print(type(degree))
print(type(likes_programming))

print(len(first_name))
print(len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
product = num_two - num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

pi = math.pi
area_of_circle = pi*pow(30,2)
circum_of_circle = 2*pi*(30) 
# radius = input('Radius: ')30
area_of_circle = pi*(pow(int(input('Radius: ')),2))
print(area_of_circle)

first_name = input('first name: ')
last_name = input('last name: ')
country = input('Country: ')
age = input('Age: ')

print(help('keywords'))