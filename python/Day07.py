#Given an array, A, of N integers, print A's elements in reverse order 
#as a single line of space-separated numbers.




#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print " ".join(map(str, arr[::-1]))
