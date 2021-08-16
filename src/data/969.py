def BFS_starting_from_one(s, Adj):  #if nodes start from one
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next1 = []
        for u in frontier:
            for v in Adj[u - 1]:  #only change from BFS
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next1.append(v)
        frontier = next1
        i += 1
    return level


n, q = map(int, input().split())
adj_list = [[] for j in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
adj_list.pop(0)
for i in range(n):
    adj_list[i].sort()
ans = BFS_starting_from_one(1, adj_list)
for i in range(q):
    c, d = map(int, input().split())
    distance = abs(ans[d] - ans[c])
    if distance % 2 == 0:
        print('Town')
    else:
        print('Road')
