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
l1.append(11)
print l1
for j in range(2,5):
    print j
print 3%2

primes = [True for j in range(5)]
primes[3] = False
primes[1] = False
print 2**(.5)
print primes
print sum(primes)

if 2 == None:
    print "Yes"

print "---------------------------------------------------------"

l = [[1], [1, 1]]
print l[1][1]

l = [k for k in range(9)]
print l
l[:3] = reversed(l[:3])
l[4:] = reversed(l[4:])
print l

l.reverse()
print l

a = 1
b = 2
a, b = b, a
print a, b
l[1], l[2] = l[2], l[1]
print l[1], l[2]
l.insert(0, float('inf'))
print l
