__author__ = 'shawn.wang'


strs = ['sas', 'sardg', 'sarp', '']

if 4 >= len(strs) or strs[4] == 's':
    print 'good'
strs.sort()
print strs
print strs[0] > strs[2]
print strs[0]
print strs[0][:2]

print " -------------The string test 2 reversed traversal--------------------------------------------------"

s = 'hello world'
print s[-1]
print s[-len(s)]
for i in reversed(s):
    print i
print "-------------------------------------------------------"

for i in reversed(range(len(s))):
    print s[i]
