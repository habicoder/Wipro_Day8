#How to Remove Letters From a String in Python
def remove_letters(string, letters_to_remove):
    result = ''
    for char in string:
        if char not in letters_to_remove:
            result += char
    return result

# Example usage:
input_string = "Hello World"
letters_to_remove = "aeiou"
result = remove_letters(input_string, letters_to_remove)
print("Original string:", input_string)
print("String after removing letters:", result)
