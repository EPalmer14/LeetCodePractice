class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        L, R = 0, len(s) - 1

        while L < R:
            if (s[L] != s[R]):
                return False
            
            L += 1
            R -= 1

        return True

        