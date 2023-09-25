#Question URl = https://leetcode.com/problems/single-number/description/

#Solution URL = https://leetcode.com/problems/single-number/solutions/2468404/python-beginner-friendly-85-fast-93-less-space/

#Using Dictionary
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k in d:
            if d[k]==1:
                return k
#Using XOR:

class Solution(object):
    def singleNumber(self, nums):
        count = 0
        for i in nums:
            count ^= i
        return count