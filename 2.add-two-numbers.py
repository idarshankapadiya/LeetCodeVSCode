#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = temp = ListNode(0)
        remainder = 0
        nodeSum = 0
        while l1 or l2:
            if l1 and l2:
                nodeSum = l1.val+l2.val+remainder
                remainder = nodeSum//10
                nodeSum = nodeSum%10
                l1 = l1.next
                l2 = l2.next
            
            elif l1:
                nodeSum = l1.val+remainder
                remainder = nodeSum//10
                nodeSum = nodeSum%10
                l1 = l1.next
                
            else:
                nodeSum = l2.val+remainder
                remainder = nodeSum//10
                nodeSum = nodeSum%10
                l2 = l2.next
                
            temp.next = ListNode(nodeSum)
            temp = temp.next
            if remainder:
                temp.next = ListNode(remainder)
        return head.next     
        
# @lc code=end

