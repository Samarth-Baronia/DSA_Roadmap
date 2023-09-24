#URL =https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(self, nums: List[int]) -> int:
    ind = 1 
    for i in range (1, len (nums)):
        if nums[i] == nums[i-1]:
            continue
        else:
            nums[ind] = nums[i]
            ind += 1
        
    return ind