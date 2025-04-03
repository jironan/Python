import datetime
 
date = datetime.date(2025,1,30)
today = datetime.date.today()
time = datetime.time(12,30,15)
current_time = datetime.datetime.now()

current_time = current_time.strftime("%H:%M:%S %m-%d-%y")

print(date)
print(today)
print(time)
print(current_time)

target_datetime = datetime.datetime(2030, 1 ,2, 12 , 30 , 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else : 
    print("Target date has not passed")