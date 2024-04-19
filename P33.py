#Sort Python Dictionaries by Key or Value

#keys

my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Sorted dictionary by keys:", sorted_dict_by_keys)

#values

my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by values:", sorted_dict_by_values)
