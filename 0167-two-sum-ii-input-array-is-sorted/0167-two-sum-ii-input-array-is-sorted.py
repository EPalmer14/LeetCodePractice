class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        out = [0] * 2
        L, R = 0, n - 1

        while (L < R):
            if (numbers[L] + numbers[R] == target):
                out[0] = L + 1
                out[1] = R + 1
                return out
            elif (numbers[L] + numbers[R] > target):
                R -= 1
            else:
                L += 1

        return out
        