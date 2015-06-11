__author__ = 'shawn.wang'

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @param {string[]} strs
    # @return {string}
    # Brute-force attack n*m
    def longestCommonPrefix1(self, strs):
        if len(strs) == 0:          # []
            return ""
        if len(strs) == 1:          # ["a"]
            return strs[0]
        i, j = 0, 0
        while 1:
            for j in range(len(strs)-1):
                if len(strs[j]) == 0 or len(strs[j+1]) == 0:    # [""]
                    return ''
                if i > len(strs[j])-1 or i > len(strs[j+1])-1 or strs[j][i] != strs[j+1][i]:
                                            # ["aa","a"]
                    return strs[0][:i]
            i = i+1


    #def longestCommonPrefix2(self, strs):



