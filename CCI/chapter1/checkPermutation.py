# True if one string is permutation of another string else False
#Approaches
# 1. Use counter function COunter(s1) == Counter(s2)
# 2. use single dictionary for 2 arrays, for s1 do s++, for s2 do s--

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    elif len(s1) == 1:
        if s1 == s2:
            return True
        return False
    dict1 ={}
    dict2 = {}
    for i in s1:
        if i in dict1.keys():
            dict1[i] +=1
        else:
            dict1[i] = 1
    for i in s2:
        if i in dict2.keys():
            dict2[i] +=1
        else:
            dict2[i] = 1
    for i in s1:
        if i not in s2:
            return False
        if dict1[i] != dict2[i]:
            return False
    return True
s1="vbbb"
s2 = "t"
print(checkPermutation(s1, s2))
    
        
