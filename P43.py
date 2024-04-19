'''lst=(23,45, [ 50,60 ], 90)

is it possible to change 50 in the list ,if yes, show the
code
'''
lst = (23, 45, [50, 60], 90)
new_tuple = tuple(lst[:2] + ([55, 60],) + lst[3:])
print(new_tuple)


