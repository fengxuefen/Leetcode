'''
Created on 2015-10-22

@author: Fen
'''
nums = [2,4,7,9]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while(left < right):
            if(sortedNums[left] + sortedNums[right] < target):
                left = left + 1
            elif(sortedNums[left] + sortedNums[right] > target):
                right = right - 1
            else:
                break
        pos1 = nums.index(sortedNums[left]) + 1
        pos2 = nums.index(sortedNums[right]) + 1
        if(pos1 == pos2):
            pos2 = nums[pos1:].index(sortedNums[right]) + pos1 + 1
        return min(pos1,pos2), max(pos1,pos2)    
s = Solution()
nums = s.twoSum(nums, 9)
