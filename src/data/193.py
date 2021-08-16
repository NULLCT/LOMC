from collections import deque

N, Q = map(int, input().split())

neighbors = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    neighbors[a - 1].append(b - 1)
    neighbors[b - 1].append(a - 1)

queries = [list(map(int, input().split())) for _ in range(Q)]

# q state: (position, parent, depth)
q = deque()
q.append((0, -1, 0))

depths = [-1] * N
parents = [-1] * N

while len(q):
    i, parent, d = q.pop()
    depths[i] = d
    parents[i] = parent
    for j in neighbors[i]:
        if parent == j:
            continue
        q.append((j, i, d + 1))

for query in queries:
    c, d = query
    if (depths[c - 1] + depths[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")