#Python program to check whether the string is Symmetrical or Palindrome
def is_symmetrical(string):
    return string == string[::-1]

def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return is_symmetrical(cleaned_string)

# Example usage:
input_string = "A man, a plan, a canal: Panama"
print("Is symmetrical:", is_symmetrical(input_string))
print("Is palindrome:", is_palindrome(input_string))
