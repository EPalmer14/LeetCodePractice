# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None or head.next is None):
            return False

        p1 = head
        p2 = head.next

        while (p2 is not None):
            if (p1 == p2):
                return True
            
            if (p2.next is not None and p2.next.next is not None):
                p2 = p2.next.next
            else:
                return False

            p1 = p1.next
        
        return False

            
        