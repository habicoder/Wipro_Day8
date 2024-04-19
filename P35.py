#Python dictionary with keys having multiple inputs

# Example dictionary with keys having multiple inputs
multikey_dict = {
    ('John', 'Doe'): 30,
    ('Jane', 'Smith'): 25,
    ('Alice', 'Johnson'): 35
}

# Accessing values using keys with multiple inputs
age_john_doe = multikey_dict[('John', 'Doe')]
print("Age of John Doe:", age_john_doe)

# Adding a new entry with a key having multiple inputs
multikey_dict[('Bob', 'Smith')] = 40

# Printing the updated dictionary
print("Updated dictionary:", multikey_dict)
