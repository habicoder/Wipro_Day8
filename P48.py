'''Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
[2:24 pm, 19/04/2024] Wipro Trainer: Use a list comprehension to iterate two lists using a for loop and concatenate the current item of each list.
'''
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)