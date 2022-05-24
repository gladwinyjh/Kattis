import heapq
from sys import stdin
from collections import deque


def main():
    pq = []

    n, t = map(int, stdin.readline().split())

    if n == 0 or t == 0:
        print(0, 0)
        return

    num_remote = 0
    num_store = 0
    
    for i in range(n):
        d, p, k = stdin.readline().split()
        
        # Intentionally give store = 0 and remote = 1 so that PQ will put store in front of remote
        if p == 'R':
            pq.append([int(d), 1, int(k)])
            num_remote += 1
        else:
            pq.append([int(d), 0, int(k)])
            num_store += 1
    
    # Take the max of 1 and number of respective prescriptions
    # So that when we take average later we wont get zero division error
    num_remote = max(1, num_remote)
    num_store = max(1, num_store)
    
    # Make pq into a priority queue
    # First priority: index 0: who comes first
    # Second priority: index 1: store or remote, since store is given 0 and remote is given 1, store comes first
    # Third priority: index 2: which one can be done quicker
    heapq.heapify(pq)
    
    # To record down total time to complete remote and store prescriptions
    total_time_remote = 0
    total_time_store = 0
    
    # Priority Queue for determining which prescription will be completed the earliest out of all the prescriptions that are being worked on
    technicians = []

    # Queues for remote and store.
    remote = deque()
    store = deque()
    
    # Fill technicians with initial prescriptions
    # Rest of prescriptions load them into respective queues
        # It is possible to load them back into pq but will have TLE when there is a need to keep loading many prescriptions back each time we check to give it to a technician
    while pq:
        entry = heapq.heappop(pq)
        if len(technicians) == t:
            if entry[1] == 1:
                remote.append(entry)
            else:
                store.append(entry)
        else:
            # Time it will finish = time it is given + time it takes to complete
            # Because this is the first batch of prescriptions, no additional waiting time is required
            time_finished = entry[0] + entry[2]
            heapq.heappush(technicians, [time_finished, entry[1], entry[2]])
    
    # Parse through remaining prescriptions
    while store or remote:
        if ((store and remote and store[0][0] <= technicians[0][0] and remote[0][0] <= technicians[0][0]) or 
                (store and remote and store[0][0] <= technicians[0][0] and remote[0][0] > technicians[0][0]) or 
                (store and remote and technicians[0][0] < store[0][0] <= remote[0][0]) or
                (store and not remote)):
            # Load from store if
                # 1) There are both store and remote left, and both of the first store and remote arrive earlier than before the earliest prescription is completed. 
                    # Always take store before remote

                # 2) There are both store and remote left, and store arrives before earliest prescription is completed and remote arrives after earliest precription is completed
                    # Next prescription available is from store, next remote have yet to arrive

                # 3) There are both store and remote left, both store and remote arrives during or after the earliest prescription is completed, but the store prescription arrives earlier than the remote one

                # 4) Only store prescriptions left; no more remote prescriptions
            entry = store.popleft()
        elif ((store and remote and store[0][0] > technicians[0][0] and remote[0][0] <= technicians[0][0]) or 
                (store and remote and technicians[0][0] < remote[0][0] < store[0][0]) or 
                (remote and not store)):
            # Load from remote if
                # 1) There are store and remote left, but store comes after earliest prescription is completed and remote comes during or before
                    # Next prescription avaiable is from remote, next store yet to arrive
                
                # 2) Therer are store and remote left, and both of them come AFTER(does not include during) the earliest prescription is completed
                    # Again, take the earlier one

                # 3) Only remote prescriptions left; no more store prescriptions
            entry = remote.popleft()
        
        # Get the additional waiting time before prescription is attended to
        wait = technicians[0][0] - entry[0]
        # If additional wait is negative, there is no wait, so 0
        wait = 0 if wait < 0 else wait
        
        # Account for the additional waiting time if any
        if entry[1] == 1:
            total_time_remote += wait
        else:
            total_time_store += wait
        
        # Pop completed prescription from technicians pq. Add time it takes to complete it
        finished = heapq.heappop(technicians)
        if finished[1] == 1:
            total_time_remote += finished[2]
        else:
            total_time_store += finished[2]
        
        # Time it will take to complete current prescription = arrival time entry[0] + completion time entry[2] + waiting time
        time_finished = entry[0] + entry[2] + wait
        # Give it to technician
        heapq.heappush(technicians, [time_finished, entry[1], entry[2]])
    
    # There may still be prescriptions that are currently being completed by technicians
    for finished in technicians:
        if finished[1] == 1:
            total_time_remote += finished[2]
        else:
            total_time_store += finished[2]
    
    print(f'{total_time_store/num_store:.6f} {total_time_remote/num_remote:.6f}')


if __name__ == '__main__':
    main()
