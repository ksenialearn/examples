#Problem D. Password Security
"""
For each test case, output one line containing Case #x: y, where x is the 
test case number (starting from 1) and y is a permutation of the entire 
uppercase English alphabet that contains no password as a continuous substring,
or the word IMPOSSIBLE if there is no such permutation.
"""
import string
alpha= string.ascii_uppercase

def findPerm(n, p):
    p= list(p)
    if n==1:
        if len(p)== 1:
            return "IMPOSSIBLE"
        
        if p[0]== 'A':
            out= 'B' + 'A' + alpha[2::]
            return out
        else:
            return out

print findPerm(1, 'X')
print findPerm(1,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')