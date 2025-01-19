class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = nums[L] + nums[i] + nums[R]
                if sum > 0:
                    R -= 1

                elif sum < 0:
                    L += 1

                else:  
                    out.append([nums[L], nums[i], nums[R]])
                    L += 1
                    
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

        return out
        