from collections import deque

n, q = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
deeply = [0 for _ in range(n)]

que = deque()
que.append((0, 0, -1))
while len(que) > 0:
    idx, deep, up = que.popleft()
    deeply[idx] = deep
    for i in edge[idx]:
        if i != up:
            que.append((i, deep + 1, idx))

for i in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    diff = abs(deeply[a] - deeply[b])
    if diff % 2 == 1:
        print("Road")
    else:
        print("Town")
