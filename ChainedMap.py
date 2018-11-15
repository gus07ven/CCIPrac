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
print("Elements:")
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))