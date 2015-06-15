__author__ = 'YangWang'


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding
# additional test cases.

class Solution:
# @param num, a list of integer
# @return an integer
    def rob(self, nums):
            if len(nums) <1:
                return 0
            if len(nums) < 2:
                return nums[0]
            dp = [nums[0], max(nums[0], nums[1])]
            i = 2
            while i < len(nums):
                dp.append(max(dp[i-1], dp[i-2]+nums[i]))
                i += 1
            return dp[-1]

nums = [0, 0, 0]
S = Solution()
print S.rob(nums)




