__author__ = 'YangWang'

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

# Hash or dictionary

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            if dict_s.get(s[i]) == dict_t.get(t[i]):
                dict_s[s[i]], dict_t[t[i]] = i, i
            else:
                return False
        return True
