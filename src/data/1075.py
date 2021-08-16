from collections import deque

n, q = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
dis = [float("inf") for i in range(n)]
done = [0 for i in range(n)]
dep = [float("inf") for i in range(n)]
dep[0] = 0

bfs = deque()
bfs.append([0, 0])
while bfs:
    node, depth = bfs.popleft()
    dep[node] = depth
    done[node] = 1
    for i in edge[node]:
        if not done[i]:
            bfs.append([i, depth + 1])

for _ in range(q):
    x, y = map(int, input().split())
    ans = dep[x - 1] + dep[y - 1]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
