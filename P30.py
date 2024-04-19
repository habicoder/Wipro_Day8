#Python – Row-wise element Addition in Tuple Matrix

def row_wise_element_addition(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums

# Example usage:
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
row_sums = row_wise_element_addition(matrix)
print("Row-wise element addition:", row_sums)
