class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        L, R = 0, n - 1

        while (L < R):
            if (numbers[L] + numbers[R] == target):
                return [L + 1, R + 1]
            elif (numbers[L] + numbers[R] > target):
                R -= 1
            else:
                L += 1

        return out
        