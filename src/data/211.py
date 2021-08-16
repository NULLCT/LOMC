import collections

INF = 10**10

N, Q = map(int, input().split())

G = [[] for _ in range(N)]
seen = [-1] * N
par = [-1] * N
todo = collections.deque()

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

todo.append(0)
seen[0] = 0
par[0] = 0

while len(todo) != 0:
    v = todo.popleft()
    for i in range(len(G[v])):
        if seen[G[v][i]] != -1:
            continue
        else:
            todo.append(G[v][i])
            seen[G[v][i]] = seen[v] + 1
            par[G[v][i]] = seen[G[v][i]] % 2

for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if par[c] == par[d]:
        print('Town')
    else:
        print('Road')
