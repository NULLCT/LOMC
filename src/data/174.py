from collections import deque

n, q = map(int, input().split())
path = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
depth = [10**6] * n
depth[0] = 0
queue = deque()
queue.append(0)
while len(queue):
    num = queue.popleft()
    for i in path[num]:
        if depth[i] == 10**6:
            depth[i] = depth[num] + 1
            queue.append(i)
for i in range(q):
    c, d = map(int, input().split())
    if (depth[c - 1] - depth[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
