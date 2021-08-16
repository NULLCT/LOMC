from collections import defaultdict, deque

n, q = map(int, input().split())
paths = defaultdict(lambda: [])

depth = [-1] * n
que = deque()
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    paths[a].append(b)
    paths[b].append(a)

depth[0] = 1
que.append(0)
while que:
    now = que.popleft()
    for v in paths[now]:
        if depth[v] != -1:
            continue
        depth[v] = depth[now] + 1
        que.append(v)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (depth[c] - depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
