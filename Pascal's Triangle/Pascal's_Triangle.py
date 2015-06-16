__author__ = 'shawn.wang'


# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        res = []
        for i in range(1, numRows+1):
            temp = [1 for j in range(i)]
            for k in range(i - 2):
                temp[k+1] = res[i-2][k] + res[i-2][k+1]
            res.append(temp)
        return res

S = Solution()
print S.generate(0)