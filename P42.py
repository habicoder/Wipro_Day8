#Check if two lists have at-least one element common

def have_common_element(list1, list2):
    # Convert one of the lists to a set
    set1 = set(list1)

    # Check if there is at least one common element
    if set1.intersection(list2):
        return True
    else:
        return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [5, 10, 15, 20]

print("List1 and List2:", have_common_element(list1, list2))
print("List1 and List3:", have_common_element(list1, list3))
