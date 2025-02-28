class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        for i, n in enumerate(nums):
            if (target - n in hashmap):
                return [i, hashmap[target - n]]

            hashmap[n] = i
                    
        