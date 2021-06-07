import sys

s1_hour, s1_min = map(int, input().split(':'))

#Convert to min
s1 = s1_hour * 60 + s1_min

s2_hour, s2_min = map(int, input().split(':'))
s2 = s2_hour * 60 + s2_min

s1_hour_interval, s1_min_interval = map(int, input().split(':'))
s1_interval = s1_hour_interval * 60 + s1_min_interval

s2_hour_interval, s2_min_interval = map(int, input().split(':'))
s2_interval = s2_hour_interval * 60 + s2_min_interval

#Create large boolean array
#Each index represents a minute, starting from 00:00 on that Saturday at index 0
arr = [0 * i for i in range(10000000)] 

#Create week array starting with Saturday
week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for i in range(s1, len(arr), s1_interval):
    arr[i] = 1


for i in range(s2, len(arr), s2_interval):
    if arr[i] == 1: #s1 will flash too

        #Get the days that passed (minutes / 60 minutes / 24 hours)
        #% 7 to get the specific day in the week, week starts from saturday
        days_passed = int((i / 60 / 24) % 7)
        print(week[days_passed])
        print("%02d:%02d" %(i/60 % 24, i%60))
        sys.exit()
    

print("Never")