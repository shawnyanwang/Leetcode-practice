__author__ = 'YangWang'

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
# this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        r = ''
        for i in range(numRows):
            j, odd = i, 1
            while j < len(s):
                r += s[j]
                if i == 0 or i == numRows - 1:
                    j += 2 * (numRows - 1)
                else:
                    if odd == 1:
                        j += 2 * (numRows - 1 - i)
                        odd = 0
                    else:
                        j += 2 * i
                        odd = 1
        return r

S = Solution()
# print S.convert("PAYPALISHIRING", 3)
# print S.convert("A", 1)
print S.convert("AB", 1)
