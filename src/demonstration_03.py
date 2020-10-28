"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Set number to the int value of txt
    number = int(txt)
    
    return number
    
print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))

# Optimized solution
def string_int2(txt):
    
    return int(txt)
    
print(string_int2("6"))
print(string_int2("1000"))
print(string_int2("12"))