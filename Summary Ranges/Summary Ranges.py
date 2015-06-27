__author__ = 'shawn.wang'

# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].



class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []

        temp =''
        res = []
        begin = end = nums[0]

        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1]+1:
                end = nums[i-1]
                if end > begin:
                    temp = str(begin)+'->'+str(end)
                else:
                    temp = str(end)
                res.append(temp)
                if i < len(nums):
                    begin = nums[i]
        return res




S = Solution()
n=[0, 1, 2, 4, 5, 7]
print S.summaryRanges(n)