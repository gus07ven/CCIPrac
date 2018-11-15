import collections

dict_one = { 'day1': 'Mon', 'day2': 'Tue'}
dict_two = { 'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict_one, dict_two)

# Creating a single dictionary
print(res.maps, '\n')

print('Keys = {}'.format((list(res.keys()))))
print('Values = {}'.format((list(res.values()))))
print()

# Print all the elements from the result
print("Printing all elements:")
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print("Find specific values in dictionary:")
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))
print()

# Adding elements to chained map
print("Adding day4 = Fri to dictionary")
dict_two['day4'] = 'Fri'
print(res.maps, '\n')
print()

# Updating element in chained map
print("Updating day2 = Sat in dictionary")
dict_one['day2'] = 'Sat'
print(res.maps, '\n')
print()
