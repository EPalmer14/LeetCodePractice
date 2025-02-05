class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        pre = strs[0]
        lenPre = len(pre)

        for s in strs[1:]:
            while pre != s[0:lenPre]:
                lenPre -= 1
                if lenPre == 0:
                    return ""
                
                pre = pre[0:lenPre]
            
        return pre
        