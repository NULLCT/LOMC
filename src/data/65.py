from collections import UserDict, deque

N, Q = map(int, input().split())
edges = {k: [] for k in range(N)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

color = [-1] * N
done = [False] * N
queue = deque([(0, 0)])

while queue:
    u, c = queue.popleft()

    if done[u]:
        continue

    done[u] = True
    color[u] = c

    for v in edges[u]:
        queue.append((v, 1 - c))

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (color[c] + color[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
