import sys
try:
    sys.setrecursionlimit(1 << 30)
    n, q = map(int, input().split())
    vector = [[] for i in range(n + 1)]
    level = [0] * (n + 1)
    query = []

    def bfs(start):
        queue = []
        vis = [False] * (n + 1)
        queue.append((start, 0))
        vis[start] = True
        while len(queue) > 0:
            now = queue.pop(0)
            level[now[0]] = now[1] + 1
            for it in vector[now[0]]:
                if vis[it]:
                    continue
                else:
                    queue.append((it, now[1] + 1))
                    vis[it] = True

    for i in range(n - 1):
        a, b = map(int, input().split())
        vector[a].append(b)
        vector[b].append(a)
    for i in range(q):
        a, b = map(int, input().split())
        query.append((a, b))
    bfs(1)
    for it in query:
        if abs(level[it[1]] - level[it[0]]) % 2 == 1:
            print('Road')
        else:
            print('Town')
except:
    pass
