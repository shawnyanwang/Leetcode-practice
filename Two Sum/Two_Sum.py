__author__ = 'shawn.wang'

# Two pointer
# 1. list sort() and index()
# 2. while loop
# 3. conditional statement
# 4. assignment and reference
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    # Two pointer

    def twoSum1(self, nums, target):
        temp = nums[:]                      # 4. assignment and reference
        temp.sort()                         # 1. list sort() and index()
        i, j = 0, len(nums)-1               # 2. while loop
        while i < j:
            if temp[i]+temp[j] == target:   # 3. conditional statement
                if nums.index(temp[i]) > nums.index(temp[j]):
                    tem = i
                    i = j
                    j = tem
                nums[nums.index(temp[i])] = None
                temp[i] = None
                return nums.index(temp[i])+1, nums.index(temp[j])+1
            elif temp[i]+temp[j] < target:
                i = i+1
            else:
                j = j-1
# 1. Initialize dictionary
# 2. get rid of current element
    # hash map

    def twoSum2(self, nums, target):
        j, dict = 0, {}                     # 1. Initialize dictionary
        for i in nums:
            dict[i] = j
            j = j+1
        j = 0
        for i in nums:
            if dict.get(target-i) != None and dict.get(target-i) != j:  # 2. get rid of current element
                return j+1, dict[target-i]+1
            j = j+1


