#Python Program to Swap Two Elements in a List
def swap_elements(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

# Example usage:
my_list = [1, 2, 3, 4, 5]
idx1, idx2 = 1, 3
swap_elements(my_list, idx1, idx2)
print(my_list)
