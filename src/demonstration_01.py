"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
def addition(a, b):
    sum = a + b
    
    return sum
    
print(addition(3, 2)) # -> 5
print(addition(-3, -6)) # -> -9
print(addition(7, 3)) # -> 10

# Optimized solution for the exercise above:
def addition2(a, b):
    return a + b

print(addition2(3, 2)) # -> 5
print(addition2(-3, -6)) # -> -9
print(addition2(7, 3)) # -> 10