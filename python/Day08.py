#Given n names and phone numbers, assemble a phone book that maps friends' 
#names to their respective phone numbers. You will then be given an unknown 
#number of names to query your phone book for. For each name queried, print
#the associated entry from your phone book on a new line in the form 
#name=phoneNumber; if an entry for name is not found, print Not found instead.




# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
dictionary = dict([raw_input().split() for i in range(n)])
for i in range(n):
    name = str(raw_input())
    if name in dictionary :
        print name+'='+str(dictionary[name])
    else :
        print 'Not found'
