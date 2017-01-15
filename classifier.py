import csv

cities= []
foodies=[]

with open('C:\Users\...\Desktop\cities/cities.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        cities.append(row[0])

with open('C:\Users\...\Desktop\cities/foodies.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        foodies.append(row[0]) 
        



with open('C:\Users\...\Desktop\cities/out.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter= ",")

    for city in cities:
        mark= False
        for foodie in foodies:
            if foodie in city:
                mark= True
        if mark== True:
            out= "yes"
        else:
            out= "no"
        
        writer.writerow([out])
