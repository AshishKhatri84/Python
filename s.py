# Pangram string
import string
def is_pangram(s):
    # Convert to lowercase and create a set of the alphabet
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    
    # Create a set of characters in the string
    letters_in_string = set(c for c in s if c in alphabet)
    
    # Compare the two sets
    return letters_in_string == alphabet

# Test cases
test_string1 = "The quick brown fox jumps over the lazy dog"
test_string2 = "Hello world!"

print(f"Is the first string a pangram? {is_pangram(test_string1)}")
print(f"Is the second string a pangram? {is_pangram(test_string2)}")