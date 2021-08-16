import queue

n, q = map(int, input().split())

g = [[] for i in range(n)]
for i in range(n - 1):
    a_i, b_i = map(int, input().split())
    a_i -= 1
    b_i -= 1
    g[a_i].append(b_i)
    g[b_i].append(a_i)

bipartite_flags = [False] * n

adj_q = queue.Queue()
adj_q.put(0)
visited = [False] * n
while not adj_q.empty():
    node = adj_q.get()
    for adj in g[node]:
        if not visited[adj]:
            bipartite_flags[adj] = not bipartite_flags[node]
            adj_q.put(adj)
            visited[adj] = True

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    print("Town" if bipartite_flags[c] == bipartite_flags[d] else "Road")
