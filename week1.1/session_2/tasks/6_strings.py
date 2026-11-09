# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # new line: outputs original string
print(f"Modified String 1: {user_string.lower()}") # outputs string in lowercase only
print(f"Modified String 2: {user_string.upper()}") # outputs string in uppercase only
print(f"Modified String 3: {user_string.strip()}") # removes trailing and leading whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces all 'a' characters with '@'
print(f"Modified String 5: {user_string.capitalize()}") # capitalises first letter of the string
print(f"Modified String 6: {user_string[::-1]}") # reverses string order
print(f"Modified String 7: {user_string.title()}") # capitalises all letters
print(f"Modified String 8: {len(user_string)}") # outputs how many characters are in the string
print(f"Modified String 9: {user_string.find('a')}") # returns index of where the first 'a' is found (-1 if not found)
print(f"Modified String 10: {user_string.count('a')}") # returns count of how many 'a' is found
print(f"Modified String 11: {user_string.startswith('Hello')}") # returns true or false if prefix matches string prefix
print(f"Modified String 12: {user_string.endswith('!')}") # returns true or false if suffix matches string suffix
print(f"Modified String 13: {user_string.isalnum()}") # returns true or false if string is only alphanumeric
print(f"Modified String 14: {user_string.isalpha()}") # returns true or false if string is only alphabetical
print(f"Modified String 15: {user_string.isdigit()}") # returns true or false if string is only digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!