#Python program to print even length words in a string
def print_even_length_words(string):
    words = string.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    for word in even_length_words:
        print(word)

# Example usage:
input_string = "Python program to print even length words in a string"
print("Even length words in the string:")
print_even_length_words(input_string)
