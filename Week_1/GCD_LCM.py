#URL = https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1

def lcmAndGcd(self, num1 , num2):
    # code here 
    a = num1
    b = num2
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
       
    lcm = (a*b) //  num1
    return lcm, num1