__author__ = 'shawn.wang'

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        dict = {'I': 1, 'V': 5, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'X': 10}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s):
                if dict[s[i]] < dict[s[i+1]]:
                    res = res - dict[s[i]]
                else:
                    res = res + dict[s[i]]
            else:
                res = res + dict[s[i]]
        return res