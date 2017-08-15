'''
One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.
'''

def items(c,i,p):

    for m in range(0, i):
        for k in range(m+1,i):
            if p[m]+ p[k] == c:
                return m+1, k+1

  

with open('C:\Users\ksaenko\Desktop\Code Jam 2010/A-large-practice.in') as r:
    with open('C:\Users\ksaenko\Desktop\Code Jam 2010/smallout1.txt','w') as out:
        count = int(r.readline())
        for case in range(count):
            c = int(r.readline())
            i = int(r.readline())
            p = r.readline().strip().split(' ')
            p= map(int,p)
            ans1,ans2 = items( c,i,p )
            
            out.write("Case #" + str(case+1) +": "+ str(ans1)+ ' '+ str(ans2) + '\n')     
        
       