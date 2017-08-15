#Problem D. Password Security
"""
For each test case, output one line containing Case #x: y, where x is the 
test case number (starting from 1) and y is a permutation of the entire 
uppercase English alphabet that contains no password as a continuous substring,
or the word IMPOSSIBLE if there is no such permutation.
"""
import string


def findPerm(n, p):
    alpha= string.ascii_uppercase
    for element in p:
        if len(element)== 1:
            return "IMPOSSIBLE"
        
        else:
            ind= alpha.find(element)
            if ind== -1:
                continue
            else:
                alpha= list(alpha)
                temp= alpha[ind]
                alpha[ind]= alpha[ind+1]
                alpha[ind+1]= temp
                alpha= "".join(alpha)
    return alpha

                

print findPerm(1, ['X'])
print findPerm(1,['ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
print findPerm(1,'XYZ GCJ OMG LMAO JK'.split(' '))
print findPerm(1,'SUBDERMATOGLYPHIC UNCOPYRIGHTABLES'.split(' '))


with open("C:\Users\ksaenko\Desktop\Google Jam\Problem D/D-small-practice-2.in") as r:
    with open('C:\Users\ksaenko\Desktop\Google Jam\Problem D/smallout2.txt','w') as out:
        count = int(r.readline())
        for case in range(count):
            numwords = int(r.readline())
            words = r.readline().strip().split(' ')
            ans = findPerm( numwords, words )
            out.write("Case #" + str(case+1) +": "+ ans+ '\n')
