import csv

cities= []
velocities= {}

with open('C:\Users\...\Desktop/velocity/cities.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        cities.append(row[0])

with open('C:\Users\...\Desktop/velocity/velocity.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        vel= row[0]
        read= row[1]
        
        velocities[vel]= read
        

out= []

with open('C:\Users\...\Desktop/velocity/out.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter= ",")

    velCities= velocities.keys()    
    print velCities
    
    for city in cities:
        mark= False
        for vel in velCities:
            if vel in city:
                mark= True
                break
            
        if mark== True:
            writer.writerow([city,velocities[vel]])
            
        else:

            writer.writerow([city, "NA"])
