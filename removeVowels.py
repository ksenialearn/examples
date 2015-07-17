#Function removeVowels() 
#search for each vowel (a,e,i,o,u) in the string 

def removeVowels(st):
	l= len(st)
	k= 0
	st1= ""
	while k<l:
		if st[k]== 'a' or st[k]== 'i' or st[k]== 'o' or st[k]== 'u' or st[k]== 'e':
			st1= st1
		
		else:
			st1= st1 + st[k]
		k= k+1
	print(st1)
