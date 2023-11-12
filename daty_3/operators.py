import math
# age = 23
# height = 1.85
# plex = complex(1, 2)

# base = input('Enter Base: ')
# height = input('Enter Height')
# print(f'The area of the triangle is {0.5*float(base)*float(height)}')

# side_a = input('Enter side a: ')
# side_b = input('Enter side b: ')
# side_c = input('Enter side c: ')
# print(f'The perimeter of the triangle is {int(side_a) + int(side_b) + int(side_c)}')

# length = input('Enter length: ')
# width = input('Enter width: ')
# print(f'Area is {length * width}')
# print(f'Perimeter is {2* (float(length) +float(width))}')

# radius = input('Enter side radius: ')
# print(f'The radius is {math.pi*radius**2}')
# print(f'The circumference is {2*math.pi*radius}')

# # Slope, x-int, y-int of y = 2x -2

# slope = 2
# x_int = 1
# y_int = -2

# # slope and eclidean distance (2,2) and (6,10)
# slope_2 = (10 - 2) / (6-2)
# e_dist = math.sqrt((6 - 2)**2 + (10 -2)**2)
# print(f'slope 1 {slope} slope 2 {slope_2}')

print(len('Python') == len('Dragon'))

print('on' in 'Python' and 'on' in 'Dragon')

print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' or 'dragon')

str(float(len('python')))

# if e_dist % 2 == 0:
#     print('even')

print(7 //3 == int(2.7))

print(type('10')== type(10))

print(int(float('9.8'))==10)

hours = input('Enter Hours: ')
rate_per_hour = input('Enter rate per hour: ')
print(f'Your weekly earning is {hours*rate_per_hour}')


years = input('Enter number of years you have lived: ')
print(f'You have lived for {60*60*24*365*years}')

for i in range(0, 5):
    print('\n')
    for j in range(0,5):
        if j == 0:
            print(i +1, end=' ')
        elif j == 1:
            print(1, end = ' ')
        else:
            print((i+1)**(j-1),end=' ')