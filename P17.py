#Python program to interchange first and last elements in a list

def interchange_first_and_last(lst):
    if len(lst) < 2:
        return lst  # No need to interchange if the list has less than two elements

    # Swap the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
interchanged_list = interchange_first_and_last(my_list)
print("Original list:", my_list)
print("Interchanged list:", interchanged_list)


