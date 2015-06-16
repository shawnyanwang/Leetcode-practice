__author__ = 'shawn.wang'

numbers = [2, 7, 11, 15, 10]
target = 9
numbers.sort()# sort
print "The numbers 1st is: ", numbers[1]
print "The length of number list is: ", len(numbers)

for i in numbers:
    print "The index %d is %d" % (numbers.index(i), i)
for i in range(len(numbers)):
    print i
i, j = 0, len(numbers)
for k in range(-1):
    print 'N'
print 'Y'

# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} target
#     # @return {integer[]}
#     def twoSum(self, nums, target):
#         for i in nums:

