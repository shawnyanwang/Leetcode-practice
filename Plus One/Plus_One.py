__author__ = 'shawn.wang'

# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        carry = (digits[-1] + 1) / 10
        digits[-1] = (digits[-1] + 1) % 10
        i = len(digits)-2
        while i > -1:
            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (temp + carry) / 10
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits

S = Solution()
print S.plusOne([8,9,9,9])