from sys import stdin


def bellman_ford(D, edgeList):
    # Bellman Ford with early termination
    for i in range(len(D)-1):
        done = True
        for (u, v, w) in edgeList:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                done = False

        if done:
            break
    
    # I dont know why but combining step below with above gives 'Wrong Answer'
    # for sample input 1 even when it gives the correct one
    # Separating it works though...
    
    # Bool list to check if vertices can be changed further
    # If can, it means that there is a cycle
    cycles = [False] * len(D)
    # Do Bellman Ford again with early termination (a lot of time saved here with early termination)
    for i in range(len(D)-1):
        cycles_detected = False
        for (u, v, w) in edgeList:
            if D[v] > D[u] + w:
                cycles_detected = True
                # Instead of changing distances, set it to '-inf' so that it will not affect other vertices
                D[v] = float('-inf')
                # Mark vertex as affected
                cycles[v] = True

        if not cycles_detected:
            break

    return cycles


def main():
    first = True
    while True:
        n, m, q, s = map(int, stdin.readline().split())

        if n == 0 and m == 0 and q == 0 and s == 0:
            return
        
        if not first:
            print()

        edgeList = []
        # Populate edge list
        for i in range(m):
            u, v, w = map(int, stdin.readline().split())
            edgeList.append((u, v, w))

        D = [float('inf')] * n
        D[s] = 0
        
        # Presence of negative weights with possibility of negative weight cycles: Bellman Ford
        cycles = bellman_ford(D, edgeList)

        for i in range(q):
            dest = int(stdin.readline())
            
            # Destination node is not reachable since distance was never updated
            if D[dest] == float('inf'):
                print('Impossible')
            
            # Cycles concerning destination node detected
            elif cycles[dest]:
                print('-Infinity')
            else:
                print(D[dest])

        first = False


if __name__ == '__main__':
    main()
