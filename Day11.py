#Calculate the hourglass sum for every hourglass in array A,
#then print the maximum hourglass sum.


#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

max=0
a=0
sum=[0 for i in range(16)]
for i in xrange(4) :
    for j in xrange(4) :

        sum[a] = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        a+=1
        #sum = sorted(sum)

print sorted(sum)[-1]
