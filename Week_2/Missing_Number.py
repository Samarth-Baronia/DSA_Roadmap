#Question URl = https://leetcode.com/problems/missing-number/description/

#Solution URl = https://leetcode.com/problems/missing-number/solutions/2521916/python-3-approaches-fast-beginner-friendly/

#Using binary search :

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        low = 0
        high= len (nums) - 1
        res = -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] > mid:
                res = mid
                high = mid -1
            else:
                low = mid + 1
        return res if res!=-1 else len(nums)
                
Solution #2 :

#Looping the range from 0 to n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i
Solution3:

#Sum of all the numbers and subtract the given array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = [i for i in range(0, len(nums)+1)]
        return sum(l) -sum(nums) 