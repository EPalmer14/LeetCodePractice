class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if(nums[i] == val):
                count += 1
        while count > 0:
            nums.remove(val)
            count -= 1
        
        return len(nums)
        