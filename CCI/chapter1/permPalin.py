#check whether a string is permutation of palindrome
# palindrome - either even count of chars should be present in string or 1 odd char is allowed
def permPalindrome(str):
    dict1 = {}
    str = str.lower()
    str = str.replace(" ","")
    for i in str:
        if i in dict1.keys():
            dict1[i] +=1
            if dict1[i]%2 ==0:
                dict1[i]=0
            else:
                dict1[i] =1
                
        else:
            dict1[i] = 1
    print(dict1)
    total = sum(list(dict1.values()))
    if total ==0 or total ==1:
        return True
    return False
str = "Tacttaa coa"
print(permPalindrome(str))