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