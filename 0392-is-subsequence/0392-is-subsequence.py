class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lngth1 = len(t)
        lngth2 = len(s)
        n, m = 0, 0
        if (lngth2 == 0):
            return True
            
        while (n < lngth1):
            if(t[n] == s[m]):
                m += 1
                if (m == lngth2):
                    return True
            n += 1
        
        if (m == lngth2):
            return True
        else:
            return False

        