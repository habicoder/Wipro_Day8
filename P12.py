import re

target_string = "12-45-78"

# Split only on the first occurrence
# maxsplit is 1
result = re.split(r"\D", target_string, maxsplit=1)

print(result)
