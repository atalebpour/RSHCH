File = open('TaxiT.csv','r')
Lines = File.readlines()
File.close()
Trips=[]
import random


for n in Lines:
    Trips.append(n.split(','))

for trip in Trips:
    pick_up=trip[5]
    drop=trip[9]
    minutes=(int(trip[10])/60)
    if pick_up==drop:
        plus=random.randint(0,15-minutes)
    else:
        plus=random.randint(0,15)
    if len(str(int(int(pick_up[-2:])+plus)))<2:
        start_minute='0'+str(int(pick_up[-2:])+plus)
    else:
        start_minute=str(int(pick_up[-2:])+plus)
    
    if len((pick_up[:-3]))<2:
        start_hour='0'+str(int(pick_up[:-3]))
    else:
        start_hour=str(pick_up[:-3])
    
        
    start_time=start_hour+':'+start_minute
    #To add by hours and minutes and don't have more than 60 minutes
    hour=int(minutes//60)
    new_minutes=minutes-hour*60
    #print(new_minutes)

    
    aux_minutes=int(start_time[-2:])+int(new_minutes)
    end_time_minutes=aux_minutes-(aux_minutes//60)*60
    end_time_hour=int(start_time[:-3])+int(hour)+(aux_minutes//60)
    
    if len(str(end_time_minutes))<2:
        end_time_minutes='0'+str(end_time_minutes)
        
    if len(str(end_time_hour))<2:
        end_time_hour='0'+str(end_time_hour)
    end_time=str(end_time_hour)+':'+str(end_time_minutes)
    #print(end_time)
    trip.insert(10, start_time)
    trip.insert(11, end_time)

import csv
newfile=open("NewTimes.csv",'w')
count=0
newfile.write('TripID,TaxiID,MonthS,DayS,YearS,Start_time,MonthE,DayE,YearE,End_time,New_Start_Time,New_End_time,Trip_Minutes\n')
for rows in range(0,50) :
    last=Trips[rows][-1].strip()
    Trips[rows].remove(Trips[rows][-1])
    Trips[rows].insert(32,last)
    print(str(Trips[rows][11]))
    newfile.write((Trips[rows][0])+','+Trips[rows][1]+','+Trips[rows][2]+','+Trips[rows][3]+','+Trips[rows][4]+','+Trips[rows][5]+','+Trips[rows][6]+','+Trips[rows][7]+','+Trips[rows][8]+','+Trips[rows][9]+','+Trips[rows][10]+','+Trips[rows][11]+','+Trips[rows][12]+','+Trips[rows][13]+','+Trips[rows][14]+','+Trips[rows][15]+','+Trips[rows][16]+','+Trips[rows][17]+','+Trips[rows][18]+','+Trips[rows][19]+','+Trips[rows][20]+','+Trips[rows][21]+','+Trips[rows][22]+','+Trips[rows][23]+','+Trips[rows][24]+','+Trips[rows][25]+','+Trips[rows][26]+','+Trips[rows][27]+','+Trips[rows][28]+','+Trips[rows][29]+','+Trips[rows][30]+','+Trips[rows][31]+'\n')

newfile.close()




            
        

     
    
    
    
