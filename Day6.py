#Given a string, S, of length N that is indexed from 0 to N-1, print its
#even-indexed and odd-indexed characters as 2 space-separated
#strings on a single line (see the Sample below for more detail).


num = int(raw_input())
for i in range (0, num) :
    string = str(raw_input())
    print string[::2]+" "+string[1::2]