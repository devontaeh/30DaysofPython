#Crate an empty tuple
empty_tuple = tuple()
#tuple of brothers and sisters
brothers = ('John','Devin','Aaron')
sisters = ('Alica','Julia','Anna')
#join
siblings = brothers + sisters
print(siblings)

print(len(siblings))

#modify tuple add names of father and mother and assign to family_members
parents = ('John','Mary')
family_members = siblings + parents

#unpack siblings and parents
siblings = family_members[0:-2]
print(siblings)
parents = family_members[-2:]
print(parents)
#Create fruits, vegetables, and anumal products tuples -> join tuples and assign it to a variable food_stuff_tp
fruits = ('Apple', 'Bananna','Peach')
vegetables = ('Cucumber', 'Tomato','Spinach')
animal_products = ('Steak','Lobster','Chicken')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#change to list

food_stuff_lt = list(food_stuff_tp)

#slice out the middle item
print(food_stuff_tp[int(len(food_stuff_tp)/2)])
#slice out first three and last three
print(f'first three:{food_stuff_tp[0:3]} last three: {food_stuff_tp[-3:]}')
#delete tuple
del food_stuff_tp
#check if items in list
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

