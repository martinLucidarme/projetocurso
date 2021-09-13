# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L = l1+l2
        L.sort()
        return L
    print(mergeTwoLists(self=0, l1=[0,2,6], l2=[2,6,8,8,7,9] ) )