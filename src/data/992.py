n, q = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(n - 1)]
g = [list() for _ in range(n)]
for (u, v) in l:
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

depth = [n] * n
depth[0] = 0
st = [0]
while st:
    v = st.pop()
    for u in g[v]:
        if depth[u] == n:
            depth[u] = depth[v] + 1
            st.append(u)

l = [tuple(map(int, input().split())) for _ in range(q)]
for (u, v) in l:
    if (depth[u - 1] + depth[v - 1]) & 1:
        print("Road")
    else:
        print("Town")
