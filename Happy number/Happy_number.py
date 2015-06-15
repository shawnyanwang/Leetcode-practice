__author__ = 'YangWang'


# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
# the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dist = {n: 1}
        while True:
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n /= 10
            if res == 1:
                return True
            if dist.get(res) > None:
                return False
            dist[res], n = 1, res



S = Solution()
L = [13, 19, 20]
for i in L:
    print S.isHappy(i)