'''Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.

Or, Iterate the list using a for loop and range() function. In each iteration, add a new key-value pair to a dict using the update() method
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)