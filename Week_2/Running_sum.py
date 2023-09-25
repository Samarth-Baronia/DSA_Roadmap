#Question URL = https://leetcode.com/problems/running-sum-of-1d-array/description/

#Solution URl = https://leetcode.com/problems/running-sum-of-1d-array/solutions/2425181/python-2-solutions-easy-to-understand-daily-leetcode/


#Solution #1 :


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range (1, len (nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums


#Solution #2 :

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = nums[0]
        for i in range (1, len (nums)):
            sums += nums [i]
            nums[i] = sums
        
        return nums