'''Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200'''

#The zip() function can take two or more lists, aggregate them in a tuple, and returns it.
#Pass the first argument as a list1 and seconds argument as a list2[::-1] (reverse list using list slicing)
#Iterate the result using a for loop
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)