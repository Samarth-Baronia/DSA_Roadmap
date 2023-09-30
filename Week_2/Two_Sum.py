#Question URL = https://leetcode.com/problems/two-sum/description/

#Solution URL = https://leetcode.com/problems/two-sum/solutions/2499736/python-2-approaches-97-fast-easy-fast/

def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range(len (nums)):
        if target - nums[i] in d :
            return [d[target - nums[i]], i]
        d[nums[i]] = i
    return [-1,-1]