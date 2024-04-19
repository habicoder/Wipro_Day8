def tuple_pair_finder(input_tuple, target_sum):
    pairs = set()
    seen = set()

    for num in input_tuple:
        complement = target_sum - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return list(pairs)

result = tuple_pair_finder((1, 2, 3, 4), 5)
print(result)

