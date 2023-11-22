#empty list
from numpy import median


lst = list()
#list with more than five items
lst_2 = [1,2,3,4,5,6]
#length of list
print(len(lst_2))
#return first, middle, last index
print(lst_2[0], lst_2[len(lst_2)//2 - 1], lst_2[len(lst_2)//2], lst_2[-1])

#declaring lsit
mixed_data_types = ['Devontae', 23,"6'2", 'single','Toronto, Ontario']
#it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])
#adding to list
it_companies[2] = 'LG'
it_companies.append('Microsoft')
it_companies.insert(len(it_companies)//2, 'Logitech')

it_companies[0] = it_companies[0].upper()
print(it_companies)

#joining items in the list
it_companies_str = '#.'.join(it_companies)
print(it_companies_str)

#checking items
print('Microsoft' in it_companies_str)

#slicing and removing
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[:3])
print(it_companies[-3:])
it_companies.pop(0)
print(it_companies)
it_companies.pop(len(it_companies)//2)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

# Joining and copying lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack_cpy = full_stack.copy()
print(full_stack_cpy)
full_stack_cpy.insert(full_stack_cpy.index('Redux')+ 1, 'Python')
full_stack_cpy.insert(full_stack_cpy.index('Redux') + 2, 'SQL')
print(full_stack_cpy)

#sort, find min/max
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = min(ages)
max = max(ages)
ages.append(max)
ages.append(min)
median_age = median(ages)

average = sum(ages) / len(ages)
range_age = max - min
abs(min - average)
abs(max-average)

print(ages, median_age, average, range_age, abs(min - average), abs(max-average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
 
]
print(countries[194//2])
if len(countries) %2 == 0:
    middle = countries[len(countries)//2 -1:len(countries)//2 +1]
else:
    middle = countries[len(countries)//2]
    
countries_pt1 = countries[:len(countries)//2]
countries_pt2 = countries[len(countries)//2:]

print(countries_pt1, countries_pt2)
print(middle)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rs, usa, *scandic = countries
print(scandic)