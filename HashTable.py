# In python hash tables are implemented with dictionaries

# Create dictionary
person_table = {'First': {'Name': 'Mark', 'Age': 7},
                'Second': {'Name' : 'Tony', 'Age': 9}}

print("Original dictionary: ")
print(person_table)
print()

# Add person to dictionary
print("Adding John to the dictionary:")
person_table['Third'] = {'Name': 'John', 'Age': 17}
print(person_table)
print()

# Update the dictionary
print("Updating second person from Tony to Mike:")
person_table['First']['Name'] = 'Mike'
print(person_table['First'])
print()

# Delete second person
print("Deleting second person from person table")
del person_table['Second']
print(person_table)



