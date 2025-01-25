# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        sumLL = ListNode()
        head = sumLL

        while(l1 is not None and l2 is not None):
            if (l1 is not None and l2 is not None):
                sumLL.val = l1.val + l2.val + carry
                print(sumLL.val)
                if (sumLL.val > 9):
                    carry = 1
                    sumLL.val -= 10
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
                if (l1 is not None or l2 is not None):
                    sumLL.next = ListNode()
                    sumLL = sumLL.next

        if (l1 is not None):
            while (l1 is not None):
                sumLL.val = l1.val + carry
                if (sumLL.val > 9):
                    carry = 1
                    sumLL.val -= 10
                else:
                    carry = 0
                l1 = l1.next
                if (l1 is not None):
                    sumLL.next = ListNode()
                    sumLL = sumLL.next

        if (l2 is not None):
            while (l2 is not None):
                sumLL.val = l2.val + carry
                if (sumLL.val > 9):
                    carry = 1
                    sumLL.val -= 10
                else:
                    carry = 0
                l2 = l2.next
                if (l2 is not None):
                    sumLL.next = ListNode()
                    sumLL = sumLL.next
        
        if (carry ==1):
            sumLL.next = ListNode()
            sumLL = sumLL.next
            sumLL.val = 1
        
        return head


