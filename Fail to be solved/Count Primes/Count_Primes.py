__author__ = 'YangWang'


# Description:
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# 1. boolean list
# 2. Sieve of Eratosthenes
# 3. check i<sqrt(n)

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes1(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        primes = [2]
        for j in range(3, n+1,2):
            for i in primes:
                if j % i == 0:
                    break
                if i >= j/2+1:
                    primes.append(j)
                    break
        # print primes
        return len(primes)

    def countPrimes2(self, n):
        if n < 2:
            return 0
        primes = [True for i in range(n+1)]
        primes[0], primes[1], primes[2] = False, False,True
        i = 2
        for i in range(2,n+1):
            if primes[i] == True:
                j = 2
                while i*j <= n:
                    primes[i*j] = False
                    j += 1
        return sum(primes)

    def countPrimes3(self, n):
        if n < 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        i = 2
        while i * i < n:
            if primes[i]:
                j = 2
                while i*j <= n:
                    primes[i*j] = False
                    j += 1
            i += 1
        return sum(primes)









S = Solution()
# print S.countPrimes2(1500000)
print S.countPrimes3(2)







