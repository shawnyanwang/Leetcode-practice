__author__ = 'YangWang'

# smart assignment
n = 10
l1 = [0 for i in range(n)]
print l1

# Two dimension

l2 = [[0 for i in range(n)] for j in range(n)]
print l2

###################################################

# reference and assignment

l = list(l1)
l[0] = 20
print l1
print l
