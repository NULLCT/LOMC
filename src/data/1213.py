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
for _ in range(Q):
    c, d = inpl()
    c -= 1
    d -= 1
    cd.append((c, d))

pool = [(0, 0)]
depth = [0] * N
parent = [-1] * N
while pool:
    x, dep = pool.pop()
    depth[x] = dep
    for y in edges[x]:
        if y == parent[x]:
            continue
        else:
            parent[y] = x
            pool.append((y, dep + 1))

for c, d in cd:
    print(output[(depth[c] + depth[d]) % 2])
