from queue import Queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(G):
    que = Queue()
    color = [-1] * N  # color is "0" or "1"
    color[0] = 0
    que.put(0)  # init
    while not que.empty():
        e = que.get()
        for v in G[e]:  # edge(e,v)
            if color[v] == -1:
                color[v] = 1 - color[e]
                que.put(v)
    return color


color = dfs(G)
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
