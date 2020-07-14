import time
from datetime import datetime

time_input = str(input("Please enter the time in HH:MM:SS format: "))
current_date = str(input("Please enter the date in YYYY/MM/DD format: "))
#strptime joins the two strings together in their same formats - %s % s needed before to indicate item in brackets are strings
selected_time = datetime.strptime('%s %s'%(current_date, time_input),"%Y/%m/%d  %H:%M:%S")
print("Time selected: ",selected_time)

#convert time to seconds
a = str(selected_time)

hours = int(a[11:13])*60*60


minutes = int(a[14:16])*60

seconds = a[17:20]

total_time_alarm = int(hours) + int(minutes) + int(seconds)

  #get current time
p = str(datetime.now().time())
    
    # convert current hours into seconds
t = p[:2]
current_hours = ((int(t)*60)*60)
    #convert current minutes into seconds
s = p[3:5]
current_minutes = int(s) * 60
    #calculate total seconds of current time
total_seconds = current_hours + current_minutes

alarm_diff = (int(total_time_alarm) - int(total_seconds))
time.sleep(alarm_diff)
print('BEEP')
