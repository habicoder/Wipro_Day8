#Python – Maximum and Minimum K elements in Tuple

import heapq

def max_min_k_elements(tuple_data, k):
    # Convert the tuple to a list
    data_list = list(tuple_data)

    # Get the k largest elements
    max_elements = heapq.nlargest(k, data_list)

    # Get the k smallest elements
    min_elements = heapq.nsmallest(k, data_list)

    return max_elements, min_elements

# Example usage:
my_tuple = (1, 5, 3, 7, 2, 9, 4, 6, 8)
k = 3
max_elements, min_elements = max_min_k_elements(my_tuple, k)
print("Maximum", k, "elements:", max_elements)
print("Minimum", k, "elements:", min_elements)
