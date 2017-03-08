#Write a factorial function that takes a positive integer, N as a parameter and
#prints the result of N!(N factorial).

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())

def factorial(n) :
    if n==1 :
        return n
    else :
        return n*factorial(n-1)

print factorial(n)
