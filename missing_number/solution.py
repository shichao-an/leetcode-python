"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
"""
def missing(a,n):
    for i in range(1,n):
        if i!=a[i-1]:
            return i
l=[1,2,3,4,6,7,8,9]
a=missing(l,len(l)+1)
print("the missing no. is",a)
