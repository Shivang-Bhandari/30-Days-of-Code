#Task :
#Given an integer,n, perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Complete the stub code provided in your editor to print whether or not  is weird.




#!/bin/python

import sys


N = int(raw_input().strip())
#Solution : 
if N%2!=0 :
    print "Weird"
else:
    if N>=2 and N<6 :
        print "Not Weird"
    elif N>=6 and N<=20 :
        print "Weird"
    elif N>=20 :
        print "Not Weird"
