def is_valid_string(s):
    return '&' in s and '#' in s and len(s) % 2 == 0
s = input("Enter a string: ")
if is_valid_string(s): 
    print("The string is valid.") 
else: 
    print("The string is not valid.") 