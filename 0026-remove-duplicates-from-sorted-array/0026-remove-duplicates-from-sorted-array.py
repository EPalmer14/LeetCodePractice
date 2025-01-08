class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for x in range(1, len(nums)):
            if(nums[x] != nums[x-1]):
                nums[index] = nums[x]
                index += 1
                
        
        
        return len(nums[:index])
            
            
        