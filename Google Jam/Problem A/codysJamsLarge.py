import csv

def solveLine(oneLine):
    
    length= len(oneLine)
    regularPrices = []
    
    for i in range(0,length):
        price= oneLine[i] * 0.75
        
        for k in range(0,length):
            if oneLine[k]== price:
                regularPrices.append(oneLine[k])
                oneLine[k]= -1
                oneLine[i]= -1
                break

    return regularPrices
    
def solveAll():
    
    fil= open("C:\Users\ksaenko\Desktop\Google Jam/A-large-practice.in")
    lines= fil.read()
    lineList= lines.split()
    
    numList = map(int,lineList)

    regularPrices= []
    count= 1
    
#    for i in range(1,len(numList)):
    i= 1
    while i< len(numList):
        tempList = []
        for j in range(i+1,i+ numList[i]*2+1):
            tempList.append(numList[j])
            tempList1= tempList
         
        tempOut= solveLine(tempList1)
        
        tempOutMod= "Case #"+str(count)+": " +" ".join(map(str, tempOut)) + "\n"

                
        
        regularPrices.append(tempOutMod)
        count+= 1
        #print tempOut
        
        i= i+ numList[i]*2+1
        #print i
    #print regularPrices

    fo = open("C:\Users\ksaenko\Desktop\Google Jam/Alarge.txt", "wb")
    line = fo.writelines(regularPrices)

        
        

            
            
solveAll()          
        
    