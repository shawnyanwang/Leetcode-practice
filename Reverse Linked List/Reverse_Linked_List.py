__author__ = 'shawn.wang'

# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        pre = None
        cur = head
        while head != None:
            nex = head.next
            head.next = pre
            cur = head
            pre = cur
            head = nex
        return cur