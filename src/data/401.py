from collections import defaultdict, deque

n, q = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


def bfs(root):
    st = root
    Q = deque()
    Q.append(st)

    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    visited[st] = True

    while len(Q) > 0:
        v = Q.popleft()
        for e in graph[v]:
            if visited[e]:
                continue
            dist[e] = dist[v] + 1
            visited[e] = True
            Q.append(e)

    return dist


dist = bfs(1)
ans = []
for _ in range(q):
    c, d = list(map(int, input().split()))
    even_odd = (dist[c] + dist[d]) % 2
    if even_odd:
        ans.append("Road")
    else:
        ans.append("Town")

for a in ans:
    print(a)
