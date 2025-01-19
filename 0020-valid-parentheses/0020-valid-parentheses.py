class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if char == ')':
                    if last != '(':
                        return False
                elif char == ']':
                    if last != '[':
                        return False
                else:
                    if last != '{':
                        return False
        
        if len(stack) != 0:
            return False

        return True

