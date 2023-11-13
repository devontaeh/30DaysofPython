str = 'thirty', 'days', 'of', 'python'
print(str)
print(' '.join(str))

str = 'Coding', 'For', 'All'
print(' '.join(str))
company = ' '.join(str)
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[6:])

substring = 'Coding'
print(company.index(substring))
print(company.rindex(substring))
print(substring in company)

company.replace('Coding', 'Python')
print(company)

company.replace('All', 'Everyone')
print(company)

company.split(' ')
print(company)
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech.split(',')
print(tech)

print(company[0])
print(company.rindex('n'))

print(company[10])

str1 ='Python For Everyone'
str2 =[ch for ch in str1 if ch.isupper()]
str2 = ''.join(str1)
print(str1)
str3 ='Coding For All'
str4 =[ch for ch in str3 if ch.isupper()]
str4 = ''.join(str3)
print(str4)

print(str3.index('C'))
print(str3.index('F'))
print(str3.rfind('I'))

grammar = 'You cannot end a sentence with because because because is a conjunction'
print(grammar.index('because'))
print(grammar.rindex('because'))
start_idx = grammar.index('because')
end_idx = grammar.rindex('e') +1 
print(grammar[:start_idx:] + grammar[end_idx:] )

print('Coding For All'.index('Coding',0))
# print('Coding For All'.index('coding',0))
sentence = '   Coding For All      '
print(sentence.rindex('All'))
print(sentence[sentence.index('Coding'):sentence.rindex('l') + 1 ])

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')
a, b = 8,6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {round(a / b,2)}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')