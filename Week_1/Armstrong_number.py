#URL = https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1


def armstrongNumber (self, n):
    # code here
    original = n
    ans = 0 
    while n :
        rem = n % 10 
        ans += rem ** 3
        n //= 10
    if ans == original :
        return "Yes"
    else:
        return "No"