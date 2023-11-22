# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#find length
print(len(it_companies))

#add twitter
it_companies.add('Twtitter')
print(it_companies)
multiple_it_companies = ['Nvidia', 'Ubisoft', 'OpenAI']
it_companies.update(multiple_it_companies)
print(it_companies)
it_companies.pop()
print(it_companies)
#remove will raise an exception if item not found, discard does
#it_companies.remove('Mozilla')
it_companies.discard('Mozilla')

#join sets
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(B.issubset(A))
print(A.isdisjoint(B))
print(A.union(B), B.union(A))
print(A.symmetric_difference(B))
del A
del B

print(len(set(age)), len(age))


'''

String is variable type that stores characters, characters can be letters, numbers, special characters

list is a set of ordered and mutable data
tuple is a set of ordered and immutable data
set is uordered and mutabable data, no duplicates

'''

#find unique words in the string
string = 'I am a teacher and I love to inspire and teach people'

str_set = set(string.split(' '))
print(str_set)
print(len(str_set))