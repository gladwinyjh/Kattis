from collections import deque


def main():
    n, m, d = map(int, input().split())
   
    # Queue for the day
    q = deque()
    # Set to check if person have been visited before
    visited = set()
    # Dictionary to store levels of skepticism for each persob
    skeptDict= {}
    # Adjacency list but dictionary
    adjDict = {}

    # Store relevant details
    for i in range(n):
        name, level = input().split()
        skeptDict[name] = int(level)
        adjDict[name] = []
    
    # Populate adjDict
    for i in range(m):
        name1, name2 = input().split()
        adjDict[name1].append(name2)
        adjDict[name2].append(name1)
    
    # Add the rumor originator (1 only) to queue
    origin = input()
    q.append(origin)
    
    # Number of days elapsed
    # Start from 1 so that
    time = 1
    while q:
        # Days passed exceeded d 
        if time > d:
            break
        
        # We want to clear all the people EACH day only 
        # So we get the length of the queue for each day and process them
        day = len(q)
        while day:
            name = q.popleft()
            # This person heard the rumor, so add his name to visited
            visited.add(name)

            for friend in adjDict[name]:
                # -1 because friend heard from name
                skeptDict[friend] -= 1
                # Friend may not have passed threshold of skepticism, but he already heard the rumor so add him to visited
                if friend not in visited:
                    visited.add(friend)
                
                # If friend heard from enough people, he can then pass the rumor
                if skeptDict[friend] == 0:
                    q.append(friend)
            
            day -= 1
        time += 1
    
    # Visited set contains people that heard the rumor, including the originator, so -1 
    # Possible that after d days, only the rumor originator knows the rumor, to prevent return value of -1 in this case, take max with 0
    print(max(0, len(visited) - 1))



if __name__ == '__main__':
    main()
