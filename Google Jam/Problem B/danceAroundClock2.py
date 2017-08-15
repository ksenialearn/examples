# -*- coding: utf-8 -*-
"""
Problem B: Dance Around the Clock

The owner of a prestigious ballroom has painted a beautiful circular clock on the dance floor, and a group of D dancers numbered 1 through D are about to literally "dance around the clock". They are standing in a circle, with dancer 1 at the 12:00 position of the circle and the other dancers going clockwise around the circle in increasing numerical order. The number of dancers is even.

The dance will go on for N turns. On the i-th turn (counting starting from 1), the following will happen:

If i is odd, then the dancer currently at the 12:00 position will swap positions with the next dancer in clockwise order. Then, going past those two, the next pair of dancers in clockwise order will swap positions, and so on, all the way around the ring clockwise, until all dancers have participated in exactly one swap.
If i is even, then the dancer currently at the 12:00 position will swap positions with the next dancer in counterclockwise order. Then, going past those two, the next pair of dancers in counterclockwise order will swap positions, and so on, all the way around the ring counterclockwise, until all dancers have participated in a swap.
For example, this diagram shows the initial state and two turns of a dance with eight people.


Which two dancers will be next to dancer number K when the dance is over?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with three integers D, K, and N: the total number of dancers, the number of one of the dancers, and the number of turns the dance will go on for.

Output

For each test case, output one line containing Case #x: y z, where:

x is the test case number (starting from 1).
y is the number of the dancer who will be standing to dancer number K's left (that is, one step away in clockwise order) when the dance is over.
z is the number of the dancer who will be standing to dancer number K's right (that is, one step away in counterclockwise order) when the dance is over.
Limits

1 ≤ T ≤ 100.
D is even.
1 ≤ K ≤ D.
Small dataset

4 ≤ D ≤ 10.
1 ≤ N ≤ 10.
Large dataset

4 ≤ D ≤ 108.
1 ≤ N ≤ 108.
Sample


Input 
 	
Output 
 
3
8 3 1
8 4 2
4 1 8

Case #1: 6 4
Case #2: 1 7
C
"""


    
    
"""

def swap(oddList, evenList, i):
    
    for t in range (1,i+1):
        # print oddList, evenList 
        newDancerList= []
        # if turn is odd,swap to the right        
        if not t%2==0:
            for j in range(0,len(evenList)):
                newDancerList.append(evenList[j])
                newDancerList.append(oddList[j])
                

            
        # if turn is even, swap to the left 
        else:
            for s in range(-1,len(evenList)-1):
                
                newDancerList.append(oddList[s])
                newDancerList.append(evenList[(s+2)% len(evenList) ])
        
        
        #print "answer after " + str(t) + " turn: ", newDancerList    
        # adjust original odd and event lists
        oddList, evenList = divide(newDancerList)
        #repeat swapping. 
    return newDancerList

def findNeighbor(dancerList, dancer):

    for i in range(0,len(dancerList)):
        if dancerList[i] == dancer:
            leftDancer= dancerList[i-1]
            rightDancer= dancerList[(i+1)%len(dancerList)]  #use % to wrap around the list
    return leftDancer, rightDancer
"""


#Read in data
print "reading data"
fil= open('C:\Users\ksaenko\Desktop\Google Jam\Problem B/B-large-practice.in')
data= fil.read()
print "data read done"
linesList= data.split()
numList= map(int, linesList)
print "data converted to numbers"

left= []
right= []
#print swap([1,3,5,7],[2,4,6,8],4)
print  numList

for k in range(1,len(numList),3):
    
    print k
    if k > 50: break
    dancerList= range(1,numList[k]+1)
 
    oddList, evenList = divide(dancerList)

    newDancerList= swap(oddList, evenList, numList[k+2])

    leftDancer, rightDancer = findNeighbor(newDancerList,numList[k+1])
    #outList += [leftDancer, rightDancer]
    left.append(leftDancer)
    right.append(rightDancer)
    
with open('C:\Users\ksaenko\Desktop\Google Jam\Problem B/last-out.txt','wb') as outFile:
    for c in range(0,len(left)):
        outFile.write("Case #" + str(c+1) + ": " + str(right[c]) + " "+ str(left[c]) + "\n")
