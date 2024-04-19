import re

target_string = "12,45,78,85-17-89"

# Define the pattern using OR (|) operator to combine two delimiters
pattern = r"-|,"

# Use re.split() with the defined pattern
result = re.split(pattern, target_string)

print(result)
