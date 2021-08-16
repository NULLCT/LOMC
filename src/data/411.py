from bisect import bisect_right

inpl = lambda: list(map(int, input().split()))
output = ['Town', 'Road']
N, Q = inpl()
edges = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = inpl()
    a -= 1
    b -= 1
    edges[a].add(b)
    edges[b].add(a)
cd = []
c2q = [set() for _ in range(N)]
for q in range(Q):
    c, d = inpl()
    c -= 1
    d -= 1
    cd.append((c, d))
    c2q[c].add(q)
    c2q[d].add(q)

FORWARD, BACK = 0, 1
pool = [(FORWARD, 0, 0)]  # s, x, dep
parent = [-1] * N
depth = [-1] * N
route = [-1] * Q
history = []
in_order = [-1] * N
cur = -1
while pool:
    s, x, dep = pool.pop()
    if s == FORWARD:
        depth[x] = dep
        cur += 1
        history.append(cur)
        in_order[x] = cur
        for q in c2q[x]:
            c, d = cd[q]
            y = d if x == c else c
            prev = in_order[y]
            if prev < 0:
                continue
            else:
                p = bisect_right(history, prev) - 1
                route[q] = depth[x] + depth[y] - 2 * p

        pool.append((BACK, x, dep))
        for y in edges[x]:
            if y == parent[x]:
                continue
            else:
                parent[y] = x
                pool.append((FORWARD, y, dep + 1))
    else:
        history.pop()

for q in range(Q):
    print(output[route[q] % 2])
# for q in range(Q):
#     print(route[q])
