"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes) -> int:  # This is just like functions in Swift when returning a type.
    seconds = minutes * 60
    
    return seconds
    
    
print(convert(5))
print(convert(3))
print(convert(2))


# Optimized implementation
def convert2(minutes: int):
    
    return minutes * 60
    
    
print(convert2(5))
print(convert2(3))
print(convert2(2))

