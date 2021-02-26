testcases = int(input())
from datetime import datetime
for _ in range(testcases):
    
    meeting_time = input()
    meeting_time_dt = datetime.strptime(meeting_time,'%I:%M %p').time()
    number_of_friends = int(input())
    
    for friend in range(number_of_friends):
        availbale_time_str = input()
        availbale_time_list = availbale_time_str.split()
        print(availbale_time_list)
        time_one = availbale_time_list[0]+" "+availbale_time_list[1]
        time_two = availbale_time_list[2]+" "+availbale_time_list[3]

        dt1 = datetime.strptime(time_one,'%I:%M %p').time()
        dt2 = datetime.strptime(time_two,'%I:%M %p').time()     
        
        if dt1 <= meeting_time_dt <= dt2:
            print("1",end=" ")
        else:
            print("0",end="")
    print()            