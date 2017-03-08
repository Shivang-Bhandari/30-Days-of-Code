#Given a base-10 integer, n, convert it to binary (base-2). Then find and print
#the base-10 integer denoting the maximum number of consecutive 1's in n's binary
#representation.


#!/bin/python

import sys

n = int(raw_input().strip())
binary=0
high=0
count=0
while n>0 :
    binary=binary*10+n%2
    n=n/2

while binary :
    z=binary%10
    binary=binary/10
    if z==1 :
        count+=1
    else :
        if count!=0 :
            high=count
        count=0
if count>high :
    high = count

print high
