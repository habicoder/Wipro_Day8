import re

target_string = "PYnative   dot.com; is for, Python-developer"

# Pattern to split: [-;,.\s]\s*
result = re.split(r"[-;,.\s]\s*", target_string)

print(result)
