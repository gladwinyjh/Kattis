import sys
# Increase recursion limit for DFS to not get RunTime Error
sys.setrecursionlimit(30000)

def dfs(person, visited, adjList, money, net):
    net += money[person]
    visited[person] = True

    for friend in adjList[person]:
        if not visited[friend]:
            net = dfs(friend, visited, adjList, money, net)

    return net

def main():
    n, m = map(int, input().split())
    adjList = [[]*n for _ in range(n)]
    money = []

    for i in range(n):
        money.append(int(input()))

    # Create adjacency list
    for i in range(m):
        firstPerson, secondPerson = map(int, input().split())
        adjList[firstPerson].append(secondPerson)
        adjList[secondPerson].append(firstPerson)

    # Visited list to flag if person is already part of a component
    visited = [False] * n
    for i in range(n):
        # Net owes/owed in this connected component (CC)
        net = 0
        if not visited[i]:
            # Do Depth First Search
            net = dfs(i, visited, adjList, money, net)

            # Within this CC, the net money is not zero
            # Someone still is owed money or owes money 
            if net != 0:
                print('IMPOSSIBLE')
                return
    
    # Traversed through everyone and net money for each CC = 0
    print('POSSIBLE')


if __name__ == '__main__':
    main()