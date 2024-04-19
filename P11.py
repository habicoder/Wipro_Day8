#Splitting strings
import re

target_string = "My name is maximums and my lucky numbers are 12 45 78"

# Split on white-space
word_list = re.split(r"\s+", target_string)

print(word_list)
