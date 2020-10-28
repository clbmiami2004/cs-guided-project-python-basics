"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# set and o and an x to zero
# Loop over the characters in the string
# do a check if it contains an "X"
    # increment the x counter
# do a check if it contains an "O"
    #increment the o counter

# check if x counter is equal to 0 counter
    # return to the caller
# otherwise
    # return False to the caller

def XO(txt):
    oCounter = 0
    xCounter = 0
    
    for character in txt:
        if character == "x":
            xCounter += 1
        elif character == "o":
            oCounter += 1
          
    return xCounter == oCounter

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))


# Optimized solution
def XO2(txt):
    # Lower case the txt
    lowerText = txt.lower()
    
    return lowerText.count("o") == lowerText.count("x")
    
print(XO2("ooxx"))
print(XO2("xooxx"))
print(XO2("ooxXm"))
print(XO2("zpzpzpp"))
print(XO2("zzoo"))
    
    