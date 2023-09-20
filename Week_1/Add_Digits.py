#URL = https://leetcode.com/problems/add-digits/description/

def addDigits(self, num: int) -> int:
    if num <= 9 :
        return num
    while num > 9:
        sums = 0 
        while num :
            sums = sums + num %10
            num//= 10
        num = sums 
    return num