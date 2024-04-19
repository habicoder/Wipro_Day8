'''Remove items from the set at once
Write a Python program to remove items 10, 20, 30 from the following set at once.

Given:

set1 = {10, 20, 30, 40, 50}
Expected output:

{40, 50}

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)
 '''
'''def unique_element_counter(elements):
    unique_element_counter = {}
    for element in elements:
        if element in unique_element_counter:
            unique_element_counter[element] += 1
        else:
            unique_element_counter[element] = 1
    return unique_element_counter


my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5]
result = unique_element_counter(my_list)
print(result)'''

def unique_element_counter(elements):
    counter = {}
    for i in elements:
        if i in counter:
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1
    return counter

my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5]
result = unique_element_counter(my_list)
print(result)