File = open('/scratch/group/talebpour/TaxiData/Taxi_Trips.csv','r')
Lines = File.readlines()
File.close()
#RowsDiv is a list of lists
RowsDiv=[]
#Separating different parameter of each trip by comma
counter11 = 0
for n in Lines:
    counter11 = counter11 + 1
    if counter11 > 2:
        RowsDiv.append(n.split(","))
	
#Replacing dash or slash by comma on dates
for i in RowsDiv:
    if i[2]!='' and i[3]!='':
        dte1=i[2]
        dte2=i[3]
        #For times that end in AM and PM    
        NoSlash1=i[2].replace("/",",")
        NoSlash2=i[3].replace("/",",")
        i.remove(dte1)
        i.remove(dte2)
        i.insert(2,NoSlash1)
        i.insert(3,NoSlash2)
        
    else:
        RowsDiv.remove(i)

#Separating dates from month, day, year and time
counter12 = 0
for i in RowsDiv:
    counter12 = counter12 + 1
    print (counter12)
    date1=i[2]
    date2=i[3]
    if date1.find(',')==2:
        separate1=date1.split(",")
        separate2=date2.split(",")
    else:
        separate1=date1.split("/")
        separate2=date2.split("/")    
####################  FOR SEPARATE1  ###

##Only do something if it fits the same format of dates
    if len(separate1)==3 and len(separate2)==3 and len(separate1[2])>10 and len(separate2[2])>10:
        if separate1[2][-2:]=='PM':
            #if separate1[2][-2:]=='PM':
            #For when it is PM and different from 12
            if separate1[2][5:7]!='12':
                time1=str(int(separate1[2][5:7])+12)+str(separate1[2][7:10])
        #When its PM and 12 dont add anything
            else:
                time1=separate1[2][5:10]

#wHEN its AM leave it like it is, unless its 12
        else:
            if separate1[2][5:7]!='12':
                time1=separate1[2][5:10]
            else:
                time1=str(int(separate1[2][5:7])-12)+str(separate1[2][7:10])
    
#####################  FOR SEPARATE2  ###
        if separate2[2][-2:]=='PM':
#For when it is PM and different from 12
            if separate2[2][5:7]!='12':
                time2=str(int(separate2[2][5:7])+12)+str(separate2[2][7:10])
#When its PM and 12 dont add anything
            else:
                time2=separate2[2][5:10]
#wHEN its AM leave it like it is, unless its 12
        else:
            if separate2[2][5:7]!='12':
                time2=separate2[2][5:10]
            else:
                time2=str(int(separate2[2][5:7])-12)+str(separate2[2][7:10])
        year1=separate1[2][:4]
        year2=separate2[2][:4]
        i.remove(date1)
        i.insert(2,separate1[0])
        i.insert(3,separate1[1])
        i.insert(4,year1)
        i.insert(5,time1)

        i.remove(date2)
        i.insert(6,separate2[0])
        i.insert(7,separate2[1])
        i.insert(8,year2)
        i.insert(9,time2)
        
        money1=i[16][1:]
        money2=i[17][1:]
        money3=i[18][1:]
        money4=i[19][1:]

        i.remove(i[16])
        i.insert(16,money1)
        
        i.remove(i[17])
        i.insert(17,money2)
        
        i.remove(i[18])
        i.insert(18,money3)
        
        i.remove(i[19])
        i.insert(19,money4)

        last=i[-1].strip()
        i.remove(i[-1])
        i.insert(30,last)
    else:
        continue
######################################
    
#Remove the dates togethet from the list and add them separated by month, day and year      


    
#Separating files according to different days
import csv
days=0
aux=0
auxlist=[]
while len(RowsDiv)>0:
    for i in RowsDiv:
        if aux==0:
            month=i[2]
            day=i[3]
            year=i[4]
            auxlist.append(i)
            RowsDiv.remove(i)
            aux=1
            days+=1
        elif month==i[2] and day==i[3] and year==i[4]:
            auxlist.append(i)
            RowsDiv.remove(i)
    newfile= open(str(month)+'_'+str(day)+'_'+str(year)+'.csv', 'w+')
    for m in auxlist:
        newfile.write('/scratch/group/talebpour/TaxiData/IndividualData/'+str(m[0])+','+str(m[1])+','+str(m[2])+','+str(m[3])+','+str(m[4])+','+str(m[5])+','+str(m[6])+','+str(m[7])+','+str(m[8])+','+str(m[9])+','+str(m[10])+','+str(m[11])+','+str(m[12])+','+str(m[13])+','+str(m[14])+','+str(m[15])+','+str(m[16])+','+str(m[17])+','+str(m[18])+','+str(m[19])+','+str(m[20])+','+str(m[21])+','+str(m[22])+','+str(m[23])+','+str(m[24])+','+str(m[25])+','+str(m[26])+','+str(m[27])+','+str(m[28])+','+str(m[29])+'\n')
    aux=0
    auxlist=[]
    newfile.close()
    
    
