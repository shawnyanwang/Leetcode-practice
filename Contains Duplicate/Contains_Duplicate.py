__author__ = 'shawn.wang'

# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            if dict.get(i) == None:
                dict[i] = 1
            else:
                return True
        return False
