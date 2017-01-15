'''
Generate 1,000 random numbers
Pick 100 randomly
Sort them
Throw out the bottom 10
Replace
Repeat until left with 100 numbers
'''
import random

numElements = 1000
List= []
numWorking = 100
bottom = 10

for i in range(0,numElements):
    num = random.randint(0,100)
    List.append(num)
 
def quicksort(List,start,end):
    if start < end:
        pivot = partition(List, start, end)
        quicksort(List, start, pivot-1)
        quicksort(List, pivot+1, end)
    return List 
 
def partition(List,start,end):
    pivot = List[start]
    left = start +1
    right = end
    done = False
    while not done:
        while left <= right and List[left] <= pivot:
            left += 1
        
        while List[right] >= pivot and right >= left:
            right -= 1
        
        if right < left:
            done = True
            
        else:
            temp = List[left]
            List[left] = List[right]
            List[right] = temp
            return right
            
 
while True:   
    workingList = []
    
    
    for j in range(0,numWorking):
        ind = random.randint(0,1000)
        num = List[ind]
        workingList.append(num)
    
    sortList = quicksort(workingList, 0, len(workingList))
    updatedList = sortList[bottom, len(sortList)]
   
