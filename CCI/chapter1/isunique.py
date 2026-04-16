# return True if all chars in string are unique
# Standard ascii characters are 128. Utmost 256.
def isUnique(s):
    if len(s)> 128:
        return False
    dict1 = {}
    for i in s:
        if i in dict1.keys():
            return False
        dict1[i] = 1
    return True
s ="abcdefght"
print(isUnique(s))