__author__ = 'shawn.wang'

# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        n, r = abs(x), 0
        while n != 0:
            r = (n % 10) + r * 10
            print bin(r)
            if r > (1 << 31):
                return 0
            n /= 10
        if x < 0:
            return -r
        return r

S = Solution()
print S.reverse(1534236469)
print bin(9646324351)

