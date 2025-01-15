class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        smallest_window = float("inf")
        L = 0
        count = 0

        for R in range(len(nums)):
            count += nums[R]

            while count >= target:
                current_window = R - L + 1
                if current_window < smallest_window:
                    smallest_window = current_window
                count -= nums[L]
                L += 1
        
        if smallest_window == float("inf"):
            return 0
        else:
            return smallest_window
            

