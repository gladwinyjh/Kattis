from sys import stdin


def main():
    while True:
        num_appointments = int(stdin.readline())
        
        if not num_appointments:
            break
        
        appointments = [] 
        for i in range(num_appointments):
            timing, time_of_day = stdin.readline().split()
            hour, minute = timing.split(':')
            hour = int(hour)
            
            # Change to 24 hr format
            # If p.m., add 12 hours IF not 12 p.m. 
            if time_of_day == 'p.m.' and hour != 12:
                hour += 12
            # If 12 a.m., change to 00
            elif time_of_day == 'a.m.' and hour == 12:
                hour = 0
            
            # New 24 hr time with minutes for sorting
            # From 0 to 2359 
            new_time = int(str(hour) + minute)
            appointments.append(new_time)
        
        appointments.sort() 
        
        for appointment in appointments:
            appointment = str(appointment)
            # 12 am
            if appointment == '0':
                print('12:00 a.m.')
            
            # 12:0X a.m., minutes that start with 0
            # Add 0 in front of minutes
            elif len(appointment) == 1:
                print('12' + ':0' + appointment[:] + ' a.m.')
            
            # 12:XX a.m., minutes do not start with 0
            elif len(appointment) == 2:
                print('12' + ':' + appointment[:] + ' a.m.')
            
            # 0X:XX a.m. 
            elif len(appointment) == 3:
                print(appointment[0] + ':' + appointment[1:] + ' a.m.')
            # 12:00 p.m. onwards
            elif int(appointment[:2]) >= 12:
                # If not 12 p.m., change back to 12 hour format
                if int(appointment[:2]) != 12:
                    old_hour = str(int(appointment[:2]) - 12)
                    print(old_hour + ':' + appointment[2:] + ' p.m.')
                else:
                    # Dont need to change, for 12:XX p.m.
                    print(appointment[:2] + ':' + appointment[2:] + ' p.m.')
            # Double digit a.m. times: 10 a.m. onwards 
            else:
                print(appointment[:2] + ':' + appointment[2:] + ' a.m.')
     
        print()


if __name__ == '__main__':
    main()
    # Process all times in 24hr format to get rid of a.m/p.m 
    # and to maintain time as a 'directional vector' from 0000 to 2359
    # Then change them back to 12hr format
    # Note corner cases when doing so
        # 1) 12 am and 12 pm
        # 2) Int conversion problems
            # Ex: 1:50 a.m. -> 150, when u want 0150
            #   : 12:21 a.m. -> 021 -> 21 when u want 0021
            #   : 12:01 a.m. -> 001 -> 1 when u want 0001