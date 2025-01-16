class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = i

            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = i

            if hashmap_s[s[i]] != hashmap_t[t[i]]:
                return False

        return True


                    