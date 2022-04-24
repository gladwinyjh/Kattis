# If statements not combined to elaborate more on the logic

# Class to make machine users
class User():
    def __init__(self, u, r, t):
        self.u = u
        self.r = r
        self.t = t
       

def main():
    # List to store Jim's timings
    jim = list(map(int, input().split()))
    # List to store machine users
    users = []

    for i in range(10):
        u, r, t = map(int, input().split())
        users.append(User(u,r,t))

    # time variable refers to when Jim can start using a machine
    time = 0
    # 3 cycles for 10 machines
    for i in range(3):
        for j in range(0, len(jim), 2):
            dur = jim[j]
            rest = jim[j+1]
            id = int(j/2)
            
            if time >= users[id].t:
                
                # It is possible that the user has done more than 1 rep since Jim leaved the machine
                # Time diff % (users[j].u + users[j].r) gives the remaining time: 0 <= remaining time < users[j].u + users[j].r
                # If the remaining time < users[j].u, that means the user is currently using the machine when Jim arrives
                # the time in which jim can use the machine becomes the difference between these 2 times
                if (time - users[id].t) % (users[id].u + users[id].r) <= users[id].u:
                    # Shift Jim's start time to after user finishes using the machine
                    time += users[id].u - (time - users[id].t) % (users[id].u + users[id].r)

                # The else statement is when user is currently resting, so Jim can use the machine
                 
                # Shift user's start time to the slot before Jim starts using the machine
                # Now users[id].t is the start time closest to when Jim can use the machine
                users[id].t = time - (time - users[id].t) % (users[id].u + users[id].r)

                # 2 situations here:
                    # 1) Time is shifted in if statement above to exactly when the user ends his workout so Jim can start his
                    # 2) Time is when user is resting, so Jim starts his workout

                # Remember that users[id].t is now adjusted to the CLOSEST before Jim uses the machine

                # Scenarios:
                    # 1) User needs to wait for Jim to finish using the machine
                    # 2) User is still resting even after Jim is done using the machine (dont need to do anything here)

                # To deal with scenario 1)
                if (time + dur) > (users[id].t + users[id].u + users[id].r):
                    users[id].t = time + dur
            
            # time < users[id].t, meaning Jim's start time is before users start time.
            else:
                # Jim arrives before user starts using machine, but user start time is during Jim is using the machine
                # Shift user start time till after Jim is done with the machine
                # The else case when user start time is before time + dur is not considered because it doesn't matter
                    # Jim uses the machine, and the user doesn't use the machine because resting/yet to begin
                if (time + dur) > users[id].t:
                    users[id].t = time + dur
            
            # Just adjust time accordingly to when Jim finishes using the machine and resting
            time += dur + rest
    
    # Not to include final resting time as per question
    print(time - jim[-1]) 


if __name__ == '__main__':
    main()
