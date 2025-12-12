def reverseString(s):
    #code here
    result=""
    for i in range(len(s)-1,-1,-1):
        result=result+s[i]
    return result

 