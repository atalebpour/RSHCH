FileName='NewTimes'
File = open(FileName+'.csv','r')
Lines = File.readlines()
File.close()
Trips=[]

###CALCULATE DISTANCE FUNCTION######
import math
from math import sin, cos, sqrt, atan2, radians
def Calculate_Distance(latt1,lonn1, latt2,lonn2):
# approximate radius of earth in km
    R = 6373.0
    lat1 = radians(float(latt1))
    lon1 = radians(float(lonn1))
    lat2 = radians(float(latt2))
    lon2 = radians(float(lonn2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    rectilinear_distance=distance*sqrt(2)
    return rectilinear_distance

## SAVE FILE INTO Trips LIST ###
for n in Lines:
    Trips.append(n.split(','))

## i,j range for the OD matrix    
i,j=78,78

## Auxiliar variable to enter save a new time if its 0 and compare with others if it's 1
aux=0

#Remove first line since are titles
Trips.remove(Trips[0])

### Start making the OD matrix
###### It will erase each trip as it counts it on a OD matrix
while len(Trips)>0:
    for trip in Trips:
        ### If aux is 0 it will create 2 OD matrix
        ## The first will save the number of trips between zones
        ## The second will save the sum of speed between zones
        if aux==0:
            OD_number_of_trips=[[ 0 for h in range(i) ] for k in range(j)]
            OD_speed=[[ 0 for h in range(i) ] for k in range(j)]
            time=str(trip[5])
            separate_time=time.split(':')
            hour=separate_time[0]
            minute=separate_time[1]
            destination=trip[17]
            origin=trip[16]
            #print("cacaaaaaaaaaaaaaaaaaaaaaaaaa")
            if destination!='' and origin!='' and trip[27]!='' and trip[30]!='':
                OD_number_of_trips[int(origin)][int(destination)]=OD_number_of_trips[int(origin)][int(destination)]+1
                coordenate1=trip[27].split(' ')
                coordenate2=trip[30].split(' ')
                lat1=coordenate1[1][1:]
                lon1=coordenate1[2][:-1]
                lat2=coordenate2[1][1:]
                lon2=coordenate2[2][:-1]
                distance=Calculate_Distance(lat1,lon1,lat2,lon2)
                time_travel=int(trip[12])/3600
                OD_speed[int(origin)][int(destination)]=OD_speed[int(origin)][int(destination)]+(distance/time_travel)
                aux=1
            else:
                aux=0
            Trips.remove(trip)
        else:
            if time==trip[5]:
                origin=trip[16]
                destination=trip[17]
                if destination!='' and origin!='' and trip[27]!='' and trip[30]!='':
                    OD_number_of_trips[int(origin)][int(destination)]=int(OD_number_of_trips[int(origin)][int(destination)])+1
                    coordenate1=trip[27].split(' ')
                    coordenate2=trip[30].split(' ')
                    lat1=coordenate1[1][1:]
                    lon1=coordenate1[2][:-1]
                    lat2=coordenate2[1][1:]
                    lon2=coordenate2[2][:-1]
                    distance=Calculate_Distance(lat1,lon1,lat2,lon2)
                    time_travel=int(trip[12])/3600
                    
                    OD_speed[int(origin)][int(destination)]=OD_speed[int(origin)][int(destination)]+(distance/time_travel)
                Trips.remove(trip)

    newfile=open(FileName+'OD_speed_average_'+str(hour)+'.'+str(minute)+'.csv' ,'w+')
    print(hour,minute)
    for rows in range(78):
        for columns in range(78):
            if rows==0 or columns==0:
                if rows==0 and columns==0:
                    newfile.write('Zone O/D Average speed')
                elif rows==0:
                    if columns!=77 :
                        newfile.write('Zone '+str(columns)+',')
                    else:
                        newfile.write('Zone '+str(columns)+'\n')

                else:
                    newfile.write('Zone '+str(rows)+',')
            elif columns!=77:
                if OD_speed[rows][columns] !=0 and OD_number_of_trips[rows][columns] !=0:
                    newfile.write(str(int(OD_speed[rows][columns])/int(OD_number_of_trips[rows][columns]))+',')
                else:
                    newfile.write('none,')
            else:
                if OD_speed[rows][columns] !=0 and OD_number_of_trips[rows][columns] !=0:
                    newfile.write(str(int(OD_speed[rows][columns])/int(OD_number_of_trips[rows][columns]))+'\n')
                else:
                    newfile.write('none\n')      
    aux=0
    newfile.close()

