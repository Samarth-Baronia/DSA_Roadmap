#URL = https://practice.geeksforgeeks.org/problems/multiply-two-strings/1

def multiplyStrings(self,s1,s2):
    # code here
    # return the product stringvalue
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    a= 0
    b = 0
    for i in s1 :
        if i == '-':
            continue
        a = a * 10 + d[i]
    for i in s2 :
        if i == '-':
            continue
        b = b * 10 + d[i]    
    
    if s1[0] == '-' and s2[0] != '-':
        return (a*b) - (2 * (a*b))
    
    elif s1[0] != '-' and s2[0] == '-':
        return (a*b) - (2 * (a*b))
    else:
        return a * b
        