#Question URL = https://leetcode.com/problems/move-zeroes/description/

#Solution URL = https://leetcode.com/problems/move-zeroes/solutions/2445904/python-2-beginner-friendly-solutions-85-fast/

Solution #1


class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i in range (len (arr)):
            if arr[i] == 0 :
                continue
            else: 
                arr[ind]= arr[i]
                ind += 1
        
        while ind < len (arr):
            arr[ind] = 0
            ind += 1


Solution #2 :


n = len (nums)
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
