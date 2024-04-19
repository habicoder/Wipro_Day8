#Reverse Words in a Given String in Python
def reverse_words(string):
    # Split the string into words
    words = string.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string

# Example usage:
input_string = "Hello World Python"
reversed_string = reverse_words(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
