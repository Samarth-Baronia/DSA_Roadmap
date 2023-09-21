#Question URL = https://leetcode.com/problems/number-of-common-factors/description/

#Solution URL = https://leetcode.com/problems/number-of-common-factors/solutions/2649364/python-brute-force-easiest-to-understand/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        for i in range (1, 1001):
            if a%i ==0 and b%i ==0 :
                c += 1
        return c


#Same approach as above, but a bit faster


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        if a > b :
            lim = a
        else:
            lim = b
        for i in range (1, lim+1):
            if a%i ==0 and b%i ==0 :
                c += 1
        return c