#URL = https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def lcmAndGcd(self, num1 , num2):
        # code here
        def find_gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        # Calculate GCD
        gcd = find_gcd(num1, num2)
        
        # Calculate LCM using the formula: LCM(a, b) = (a * b) / GCD(a, b)
        lcm = (num1 * num2) // gcd
        
        return lcm, gcd
                