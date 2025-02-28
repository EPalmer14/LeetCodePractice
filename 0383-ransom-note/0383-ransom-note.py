class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}

        for char in magazine:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in ransomNote:
            if char not in hashmap or hashmap[char] <= 0:
                return False
            else: 
                hashmap[char] -= 1
        
        return True

        
        