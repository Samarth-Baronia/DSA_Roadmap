#Question URL = https://leetcode.com/problems/smallest-even-multiple/description/

#Solution URL = https://leetcode.com/problems/smallest-even-multiple/solutions/4071407/python-simple-solution-o-n-2-84-faster-97-less-space/


def smallestEvenMultiple(self, n: int) -> int:
    if n % 2 == 0 :
        return n 
    for i in range (2, (n*2) + 1, 2):
        if i % 2 == 0 and (n % i == 0 or i % n == 0) :
            return i