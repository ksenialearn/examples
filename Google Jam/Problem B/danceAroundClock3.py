
def findDancers(dancers,dancer,turns):
    if not dancer%2==0: # if dancer is not even
        dancerPosition= (dancer + turns) % dancers 
        dancer1= (dancerPosition + turns+1) % dancers
        dancer2= (dancerPosition + turns-1) % dancers
        
    else:
        dancerPosition= (dancer - turns) % dancers
        dancer1= (dancerPosition - turns+1) % dancers
        dancer2= (dancerPosition - turns-1) % dancers
    
    if dancer1 == 0: dancer1 = dancers
    if dancer2 == 0: dancer2 = dancers
    return dancer1, dancer2
    
    
print findDancers(8,3,1)
print findDancers(8,4,2)
print findDancers(4,1,8)

fil= open('C:\Users\ksaenko\Desktop\Google Jam\Problem B/B-large-practice.in')
data= fil.read()
print "data read done"
linesList= data.split()
numList= map(int, linesList)
print "data converted to numbers"

with open('C:\Users\ksaenko\Desktop\Google Jam\Problem B/last-out.txt','wb') as outFile:
    for k in range(1,len(numList),3):
        y, z = findDancers( numList[k], numList[k+1], numList[k+2] )
        x = (k-1) / 3 + 1
        outFile.write("Case #" + str(x) + ": " + str(y) + " "+ str(z) + "\n")
        