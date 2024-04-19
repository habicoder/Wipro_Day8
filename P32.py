#Python program to create a list of tuples from given list having number and its cube in each tuple

def create_tuple_list(numbers):
    tuple_list = [(num, num ** 3) for num in numbers]
    return tuple_list

# Example usage:
numbers = [1, 2, 3, 4, 5]
tuple_list = create_tuple_list(numbers)
print("List of tuples:", tuple_list)
