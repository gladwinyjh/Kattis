from sys import stdin
from collections import deque, defaultdict


def BFS(q, visited, adj_list):
    count = 1
    step = 1
    # BFS one step at a time
    while q:
        # Don't need to explore past step 6
        if step > 6:
            break
        
        q_length = len(q)
        while q_length:
            u = q.popleft()

            for v in adj_list[u]:
                if not visited[v]:
                    visited[v] = 1
                    count += 1
                    q.append(v)
            
            q_length -= 1

        step += 1
    
    return count


def main():
    T = int(stdin.readline())
    
    while T:
        M = int(stdin.readline())

        adj_list = defaultdict(list)

        # Dictionary to store hashed addresses to integers
        # Gonna get TLE if don't!!!
        devices = {}
        device_id = 0
        for i in range(M):
            u, v = stdin.readline().split()
            
            # Hash u to device_id
            if u not in devices:
                devices[u] = device_id
                device_id += 1

            # Hash v to device_id 
            if v not in devices:
                devices[v] = device_id
                device_id += 1

            adj_list[devices[u]].append(devices[v])
            adj_list[devices[v]].append(devices[u])
        
        # Number of address not permitted
        not_allowed = 0
        # Boolean flag for early termination
        exceeded = False
        # BFS from each device one at a time
        # Check if all other devices can be visited within 6 steps
        for device in devices.values():
            visited = [0] * device_id
            visited[device] = 1 
            q = deque([device])
            
            # Returns number of reachable devices from current devicee
            reachable = BFS(q, visited, adj_list)
            
            # Not all devices can be reachable, increment not_allowed
            if reachable < len(devices):
                not_allowed += 1
            
            # Early termination if number of addresses exceed permitted 5%
            if not_allowed > 0.05 * len(devices):
                exceeded = True
                break
        
        if exceeded:
            print('NO')
        else:
            print('YES')
        
        T -= 1


if __name__ == '__main__':
    main()
