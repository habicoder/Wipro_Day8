#Handling missing keys in Python dictionaries

my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('d', 'Key not found')
print("Value:", value)
