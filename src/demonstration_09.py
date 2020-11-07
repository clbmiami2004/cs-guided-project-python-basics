"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    # Your code here
    myDict2 = {}
    
    for letter in letters:
        bob = letter.lower()
        dave = letter.upper()
        myDict2[bob] = dave
        # {bob: "dave"}
    
    return myDict2

print(mapping(["p", "s"]))

