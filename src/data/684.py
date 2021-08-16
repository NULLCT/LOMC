import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N - 1)]
CD = [tuple(map(int, input().split())) for i in range(Q)]

es = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    es[a].append(b)
    es[b].append(a)

depth = [0] * N
visited = [0] * N
visited[0] = 1
stack = [0]
while stack:
    v = stack.pop()
    for to in es[v]:
        if visited[to]: continue
        visited[to] = 1
        depth[to] = depth[v] + 1
        stack.append(to)

ans = []
for c, d in CD:
    c, d = c - 1, d - 1
    x = depth[c] + depth[d]
    ans.append('Road' if x % 2 else 'Town')
print(*ans, sep='\n')
