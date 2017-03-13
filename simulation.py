
File = open('NewTimes2.csv','r')
Lines = File.readlines()
File.close()
Trips=[]
Trips2=[]
for n in Lines:
    Trips.append(n.split(';'))
    Trips2.append(n.split(';'))

# Make a list of all taxi id and zeros
#The zeros is where the starting coordinates should be, so with the 0 we know we have to assign a starting coordenate
aux=0
taxis_id=[]
number_of_taxis=0
list_aux=[]
while len(Trips)>0:
    for trip in Trips:
        taxid=str(trip[1])
        if not taxid in taxis_id:
            list_aux.append(trip[1])
            list_aux.append(['0','0'])
            number_of_taxis+=1
            taxis_id.append(list_aux)
        Trips.remove(trip)
        list_aux=[]


###A function to convert time into minutes so its easier to handle
def Change_to_minutes (time):
    minute=int(time[-2:])
    hour=int(time[:-3])
    minutes=hour*60+minute
    return minutes

##The class trips that have all the information we are going to need for assignation
class Trips_Info:
    def __init__(self, ID,start,travel,origin,destination,lat1,lon1,lat2,lon2,taxi):
        self.ID=ID
        self.start_time=Change_to_minutes(start)
        self.travel_time=int(travel)/60
        self.origin_zone=origin
        self.destination_zone=destination
        self.latitude_pickup=lat1
        self.longitude_pickup=lon1
        self.latitude_drop=lat2
        self.longitude_drop=lon2
        self.taxi=taxi

#Make a list with the trips, saving the class. So then if i call a trip I can ask a particular variable form it easier
#The last part of each trip has a 0 that means it havent been assigned to any taxi
#I also made another normal list that just saves the data, but don't know if will be necesary
Trips_info=[]
Trips_info2=[]
aux_list=[]
counter=0
for t in Trips2:
    #This is to avoid getting errors for empty data
    if len(t[0])>10 and len(t[27])>5 and len(t[30])>5 and t[12]!='' and t[16]!='' and t[17]!='':
        coordenate1=t[27].split(' ')
        coordenate2=t[30].split(' ')
        lat1=coordenate1[1][1:]
        lon1=coordenate1[2][:-1]
        lat2=coordenate2[1][1:]
        lon2=coordenate2[2][:-1]
        trip=Trips_Info(t[0],t[10],t[12],t[16],t[17],lat1,lon1,lat2,lon2,'0')
        aux_list.append(t[0])
        aux_list.append(t[10])
        aux_list.append(t[11])
        aux_list.append(t[12])
        aux_list.append(t[16])
        aux_list.append(t[17])
        coordenate1=t[27].split(' ')
        coordenate2=t[30].split(' ')
        lat1=coordenate1[1][1:]
        lon1=coordenate1[2][:-1]
        lat2=coordenate2[1][1:]
        lon2=coordenate2[2][:-1]
        aux_list.append(lat1)
        aux_list.append(lon1)
        aux_list.append(lat2)
        aux_list.append(lon2)
        aux_list.append('0')
        if not '' in aux_list:
            Trips_info.append(trip)
            Trips_info2.append(aux_list)
        aux_list=[]

        
#########  CALCULATE DISTANCE ##########
#Function to calculate distance.
#I took it directly by google and multiplied the result by sqr(2) to get the rectangular distance
import math
from math import sin, cos, sqrt, atan2, radians
#This is with equirectangular approximation?
def Calculate_Distance(latt1,lonn1, latt2,lonn2):
# approximate radius of earth in km
    R = 6373.0
    lat1 = radians(latt1)
    lon1 = radians(lonn1)
    lat2 = radians(latt2)
    lon2 = radians(lonn2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


########    AVERAGE SPEED   ########
#This function is to get the average speed between 2 zones
#It is suposed to be by every 15 minutes but I need good data to hace that
#I used a matrix with random data from 1 to 100
#When get the data this funtion will get more complicated, and will need start_time besides origin and destin
def Get_Average_speed(origin,destination):
    file=open('OD_RANDOM.csv','r')
    matrix=[]
    for line in file:
        matrix.append(line.split(','))
    average_speed=matrix[int(origin)][int(destination)]
    return average_speed

#Starting to assign taxis to trips
#The messy part
Taxis_assign=[]
Taxis_times=[]
assigned_trips=0
trips_in_taxi=[]
from random import randint
#while assigend_trips< len(Trips_info):
#This is only for testing
while assigned_trips<1:
    for tnum in range(len(taxis_id)):
        if taxis_id[tnum][1][0]=='0':
            Assigning=taxis_id[tnum][0]
            earliest=999999999999
            count=0
            for every_trip in Trips_info:
                time=every_trip.start_time
                if time<earliest and every_trip.taxi=='0':
                    earliest=time
                    earliest_id=every_trip.ID
                    Index=count
                count+=1
            Trips_info[Index].taxi=Assigning
            assigned_trips+=1
            taxis_id[tnum][1][0]=Trips_info[Index].latitude_pickup
            taxis_id[tnum][1][1]=Trips_info[Index].longitude_pick
            assigned_trips+=1
            trips_in_taxi=[]
            interval_occupied=[]
            trips_in_taxi.append(Trips_info[Index])
            starting=Trips_info[Index].start_time
            finishing_min=int(Trips_info[Index].travel_time)+int(Trips_info[Index].start_time)
            interval_occupied.append([starting,finishing])
        for tripss in Trips_info:
            if tripss.taxi=='0':
                last_
                
            
    




