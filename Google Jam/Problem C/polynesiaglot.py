# Problem C. Polynesiaglot
"""
All words consist of letters. Letters are either consonants or vowels.
Any consonant in a word must be immediately followed by a vowel.

If Ursula's new language has C different consonants and V different vowels available to use, 
then how many different valid words of length L are there in her language? 

Since the output can be a really big number, we only ask you to output the remainder 
of dividing the result by the prime 109+7 (1000000007).
"""
memos= {}

def numberWordsBrute(c, v, l, isvowel):
    count= 0

    key = (c,v,l,isvowel)
    if key in memos:
        return memos[key]
        
    if l==1:
        count= v
        
    else: 
           
        if isvowel:
            count+= v*numberWordsBrute(c,v,l-1,True)
            count+= c*numberWordsBrute(c,v,l-1,False)
            
       
        else:
            count+= v*numberWordsBrute(c,v,l-1,True)

    memos[key] = count                       
    return count

def numberWords(c, v, l):
    numWords= numberWordsBrute(c,v,l,True)%(10**9+7)
    return numWords
    

#print numberWords(1,1,4)
#print numberWords(1,2,2)

with open('C:\Users\ksaenko\Desktop\Google Jam\Problem C/C-large-practice.in') as fil:
    lines= fil.read()
    
linesList= lines.split()
numList= map(int, linesList)

with open('C:\Users\ksaenko\Desktop\Google Jam\Problem C/C-small1-out.in','wb') as outFil:
    for i in range(1,len(numList),3):
        num= numberWords(numList[i],numList[i+1],numList[i+2])
        outFil.write('Case #' + str((i-1)/3+1) + ': '+ str(num)+"\n")
