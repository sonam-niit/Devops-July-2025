from datetime import datetime,date

now = datetime.now()
print("Date & Time" ,now)
print("Date: ",now.date()) #extract date only
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)
print("Hour: ",now.hour)
print("Minutes: ",now.minute)

print(date.today()) #use date object and today() to get current date 

myday=date(2023,12,25)
print('Specific Date: ',myday)

print("By Default",now)
print("Format: ",now.strftime("%Y/%m/%d %H:%M:%S"))
## strftime -- string format means convert date object to String


##Parse
##strptime converts str to date object
date_str="2025-05-03"
date_ob=datetime.strptime(date_str,"%Y-%m-%d")
print(date_ob)
