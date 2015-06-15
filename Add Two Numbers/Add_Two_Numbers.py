__author__ = 'YangWang'


# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
# of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers1(self, l1, l2):
        res = ListNode(0)
        h = res
        carry = 0
        while l1 !=None or l2 !=None:
            if l1 == None:
                n = l2.val + carry
                l2 = l2.next
            elif l2 == None:
                n = l1.val + carry
                l1 = l1.next
            else:
                n = l1.val + l2.val + carry
                l1 ,l2 = l1.next, l2.next
            carry = n/10
            digit = n%10
            nex = ListNode(digit)
            h.next = nex
            h = nex
        if carry == 1:
            nex = ListNode(1)
            h.next = nex

        return res.next

    def addTwoNumbers2(self, l1, l2):
        h1 = l1
        h2 = l2
        carry = 0
        i = j = 0
        while h1 !=None:
            h1=h1.next
            i += 1
        while h2 !=None:
            h2=h2.next
            j += 1
        if i < j:
            res = l2
            h1 = l2
            h2 = l1
        else:
            res = l1
            h1 = l1
            h2 = l2
        cur = h1
        while h1 > None:
            cur = h1
            if h2 == None:
                n = h1.val + carry
                h1 = h1.next
            else:
                n = h1.val + h2.val + carry
                h1 ,h2 = h1.next, h2.next
            carry = n/10
            digit = n%10
            cur.val = digit
        if carry == 1:
            nex = ListNode(1)
            cur.next = nex
        return res

    def addTwoNumbers3(self, l1, l2):

        n1 = n2 =0
        i = 0
        while l1 !=None:
            n1 += 10**i*l1.val
            l1=l1.next
            i += 1
        i = 0
        while l2 !=None:
            n2 +=  10**i*l2.val
            l2=l2.next
            i += 1
        n = n1 + n2
        h = ListNode(n%10)
        n /= 10
        res = h
        while n > 0:
            h.next = ListNode(n%10)
            h = h.next
            n /= 10

        return res

