class Solution(object):  
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNextN(n):
            out = 0
            while n:
                d = n%10
                out += d**2
                n = n//10
            
            return out

        seenNumbers = set()

        while n not in seenNumbers:
            seenNumbers.add(n)
            n = getNextN(n)
            if n == 1:
                return True
    
        return False
    

        
        