from collections import deque

n, q = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
color = [-1 for _ in range(n)]
queue = [(0, 0)]
queue = deque(queue)
while queue:
    v, c = queue.popleft()
    color[v] = c
    for nex in tree[v]:
        if color[nex] == -1:
            queue.append((nex, (c + 1) % 2))
# print(color)
for _ in range(q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
