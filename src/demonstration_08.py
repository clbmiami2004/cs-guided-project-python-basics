"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
# def num_args():
#     # Your code here


def csWhereIsBob(names):
    
    for name in names[0:]:
        if name == names["Bob"]:
            myName = name
            return myName
        else:
            return "Nothing found"
    return -1

print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))