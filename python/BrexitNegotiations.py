from sys import stdin
from heapq import *


def main():
    n = int(stdin.readline())
    
    # Keep track of base time needed to complete topic at each index
    time_list = []
    # Keep track of the topics that are needed to be covered before discussion of topic at index
    indegree_topics = [[] for _ in range(n)]
    # Keep track of the number of outgoing edges for topic at each index
    adj_list = [0] * n
    
    for i in range(n):
        time, num_topics, *topics = map(int, stdin.readline().split())
        time_list.append(time)
        if num_topics:
            for x in topics:
                indegree_topics[i].append(x-1)
                adj_list[x-1] += 1
    
    # Use PQ to keep ordering of the times
    # Min-heap, so build topo order from the back
    # Smallest time needed goes to the back, next smallest goes before that, ...
    pq = []

    # Go through adjacency list
    # This is directed graph, so if adj_list[x] is empty, x has no outgoing edges
    # So x should be placed near/at the end of the topo order
    # Use PQ to prioritise smaller times to be popped first to be placed at the back of the order
    [heappush(pq,((time_list[idx], idx))) for idx, x in enumerate(adj_list) if x == 0]

    # Keep track of the minimum length of longest
    min_length = 0
    # Keep track of number of topics placed
    # Start with 1 for first topic placed
    count = 1
    
    # Modified Kahn's Algorithm
    while pq:
        time, x = heappop(pq)
        
        # Update min_length
        # (n - count) refers to the number of topics to be discussed before this topic
            # Remember we are building the order from the back
        # So total time = time + (n - count)
        min_length = max(min_length, time+n-count)
        
        for pred in indegree_topics[x]: # Get the predecessor topics for topic x
            # -1 neighbour for this predecessor as x is being processed now
            adj_list[pred] -= 1
            if not adj_list[pred]:
                # This predecessor has no more outgoing edges
                # Can be enqueued in PQ now
                heappush(pq, ((time_list[pred], pred)))
        
        # One more topic placed to the back
        count += 1

    print(min_length)


if __name__ == '__main__':
    main()
    # Topo sort
        # The longer the meeting, the more you want to push it closer to the front
        # so that the longest of all the meetings can be minimised
        # Ex:
            # 1) Meeting that takes up 4 units that is placed after 3 meetings is 
            # Prefered over the 2) same meeting that is placed after 5 meetings
                # 1) length: 4+3=7 units
                # 2) length: 4+5=9 units (longer)

            # Do so while maintaining topological order
