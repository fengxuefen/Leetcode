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
        valuedic = {}
        for index in range(len(nums)):
            if target - nums[index] in valuedic:
                return min(index + 1,valuedic[target - nums[index]] + 1),max(index + 1,valuedic[target - nums[index]] + 1)
            valuedic[nums[index]] = index