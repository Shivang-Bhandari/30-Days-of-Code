#Given an integer,n, print its first 10 multiples. Each multiple
#nxi(where 1<=i<=10) should be printed on a new line in the
#form: n x i = result.

#Solution :

#!/bin/python

import sys


n = int(raw_input().strip())
for i in range(1,11) :
    x=str(i*n)
    print str(n)+" x "+str(i)+" = "+x
