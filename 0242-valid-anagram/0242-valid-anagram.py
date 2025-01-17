class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = {}
        hashmap_t = {}

        for char_s in s:
            if char_s not in hashmap_s:
                hashmap_s[char_s] = 1 
            else:
                hashmap_s[char_s] += 1
        
        for char_t in t:
            if char_t not in hashmap_t:
                hashmap_t[char_t] = 1
            else:
                hashmap_t[char_t] += 1

        for char in hashmap_s:
            if (char not in hashmap_t or hashmap_s[char] != hashmap_t[char] or len(hashmap_s) != len(hashmap_t)):
                return False
        
        return True
        