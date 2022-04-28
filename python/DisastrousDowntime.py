import math
from collections import deque


def main():
    # Use a queue to keep track of the number of current requests running
    requestsQueue = deque()

    n, k = map(int, input().split())
    
    # Collect first request
    first = int(input())
    requestsQueue.append(first)
    
    # maxQueueSize is used to keep track of the maximum number of concurrent requests 
    maxQueueSize = 1
    for i in range(1, n):
        request = int(input())
        
        # While there are still requests and the first request in the queue is done by the time 
        # this new request comes in, dequeue the old request
        while requestsQueue and requestsQueue[0] + 1000 <= request:
            requestsQueue.popleft()
        
        # Add this new request to the queue
        requestsQueue.append(request)

        # Keep track of the maximum number of requests running concurrently
        # The max number of concurrent requests need not always be during the last request
        maxQueueSize = max(maxQueueSize, len(requestsQueue))
    
    # Get the number of servers needed by dividing by k
    # Round up as cannot have part of a server
    print(math.ceil(maxQueueSize/k))


if __name__ == '__main__':
    main()
