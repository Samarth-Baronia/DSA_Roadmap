#Question URL = https://leetcode.com/problems/3sum/description/

#Solution URL = https://leetcode.com/problems/3sum/solutions/2546499/python-beginner-friendly-two-pointers/

def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len (nums) < 3:
        return []
    nums.sort()
    ans = []
    for cur_ind in range (len (nums)-1):
        if cur_ind > 0 and nums[cur_ind] == nums[cur_ind - 1]:
            continue
        left, right = cur_ind + 1, len(nums)-1 
        while left < right :
            threesum = nums[cur_ind] + nums[left] + nums[right]
            if threesum > 0 :
                right -= 1
            elif threesum < 0 :
                left += 1
            else:
                ans.append([nums[cur_ind], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right :
                    left += 1
    return ans

    
#Below solution is just replica of above with enumerate function



def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len (nums) < 3:
        return []
    nums.sort()
    ans = []
    for cur_ind, cur_num in enumerate(nums):
        if cur_ind > 0 and cur_num == nums[cur_ind - 1]:
            continue
        left, right = cur_ind + 1, len(nums)-1 
        while left < right :
            threesum = cur_num + nums[left] + nums[right]
            if threesum > 0 :
                right -= 1
            elif threesum < 0 :
                left += 1
            else:
                ans.append([cur_num, nums[left], nums[right]])
                left += 1
				
				#To avoid the repetitive elements
                while nums[left] == nums[left - 1] and left < right :
                    left += 1
    return ans