# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergedList = ListNode()
        head = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            
            mergedList = mergedList.next
        
        if list1:
            mergedList.next = list1
        else:
            mergedList.next = list2

        return head.next
        