"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hash = {None:None}
        copy = Node(0)
        copyReturn = copy
        current = head
        
        while current:
            tmp = Node(current.val)
            hash[current] = tmp
            current = current.next
        
        current = head

        while current:
            copy.next = hash[current]
            copy = copy.next
            copy.next = hash[current.next]
            copy.random = hash[current.random]
            current = current.next

        return copyReturn.next
