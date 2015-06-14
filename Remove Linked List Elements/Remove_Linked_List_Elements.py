__author__ = 'YangWang'

# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements1(self, head, val):   # fail
        if head == None:
            return None
        cur = head.next
        pre = head
        nex = head.next
        while cur != None:
            nex = cur.next
            if cur.val == val:
                pre.next = nex
            else:
                pre = cur
            cur = nex
        if head.val == val:
            return None
        return head

    def removeElements2(self, head, val):

        Abhead = ListNode(None)
        Abhead.next = head
        pre = Abhead
        cur = head
        while cur != None:
            nex = cur.next
            if cur.val == val:
                pre.next = nex
            else:
                pre = cur
            cur = nex
        return Abhead.next



list = [1, 2, 6, 3, 4, 5, 6]

head = ListNode(list[0])
h = head
for i in range(1,len(list)):
    h.next = ListNode(list[i])
    h = h.next

S = Solution()

print S.removeElements2(head, 6)

while head != None:
    print head.val
    head = head.next

