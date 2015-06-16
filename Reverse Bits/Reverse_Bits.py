__author__ = 'shawn.wang'


# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary as
# 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer


class Solution:
    # @param n, an integer
    # @return an integer
    # 448
    def reverseBits1(self, n):
        n1 = 1 << 31
        res = 0
        for i in range(32):
            print i, (n & n1)
            res += (n & n1) >> (31-i)
            print res
            n <<= 1
        return res

    # 544 ms
    def reverseBits2(self, n):
        n1 = 1
        res = 0
        for i in range(32):
            print i, (n & n1)
            res += (n & n1) << (31-i)
            print res
            n >>= 1
        return res

    # divid and conquer 76 ms
    def help_3(self, n, m):
        if m == 1:
            return n
        n1 = self.help_3(n >> (m/2), m/2)
        n2 = self.help_3(n & (2**(m/2)-1), m/2)
        return n1+(n2 << (m/2))



    def reverseBits3(self, n):
        return self.help_3(n, 32)







S = Solution()
n = 0
print bin(n)
print bin(S.reverseBits3(n))
print S.reverseBits3(n)
print '--------------------------------------------------------------------'
n = 0b11111111111111110000000000000000
m = 32
n1 = n >> (m/2)
n2 = n & (2**(m/2)-1)
print bin(n >> (m/2))

print bin(n & (2**(m/2)-1))
print bin(n1+(n2 << (m/2)))
