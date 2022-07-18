from sys import stdin
from collections import defaultdict, deque


def main():
    n, m = map(int, stdin.readline().split())
    
    targets = set(stdin.readline().split())

    adj_list = defaultdict(list)
    for i in range(m):
        l1, l2, c = stdin.readline().split()
        adj_list[l1].append((l2, int(c)))
        adj_list[l2].append((l1, int(c)))
    
    q = deque(['English'])
    visited = set()
    visited.add('English')
    
    # Dictionary to store smallest cost from English to a language
    cost_dict = defaultdict(lambda: float('inf'))
    cost_dict['English'] = 0

    # BFS from English
    while q:
        q_length = len(q)
        
        curr_iter = set()
        # Process all nodes within this edge number
        while q_length:
            lang = q.popleft()

            for other_lang, cost in adj_list[lang]:
                # If language is in visited, it has already been explored in previous iterations
                    # Previous iterations have less number of edges
                        # Since priorizing edge numbers, do not process anymore since this will have more edges
                if other_lang in visited:
                    continue
                
                # First time visiting language in this iteration
                if other_lang not in curr_iter:
                    # Add language to current iteration
                    curr_iter.add(other_lang)
                    # Only append language once as only concerned with shortest distance to language each iteration
                    q.append(other_lang)

                if lang in targets:
                    # Previous language was a target language, so can use the same translator (0 cost) + current cost
                    cost_dict[other_lang] = min(cost_dict[other_lang], cost)
                else:
                    # Have to pay for cost all the way
                    cost_dict[other_lang] = min(cost_dict[other_lang], cost_dict[lang] + cost)
             
            q_length -= 1

        for x in curr_iter:
            # Only add those languages visited to visited after each iteration
            # as it is possible to visit same language within a iteration
            visited.add(x)
    
    total_cost = 0
    for target in targets:
        if target not in cost_dict:
            print('Impossible')
            return
        
        total_cost += cost_dict[target]
    
    print(total_cost)


if __name__ == '__main__':
    main()
