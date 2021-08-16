n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)


# graph and n is necessary
def dfs(start):
    par = [-1] * n
    depth = [-1] * n
    euler = []
    stack = []
    stack.append(start)
    depth[start] = 0
    while stack:
        v = stack.pop()
        euler.append(v)
        d = depth[v]
        for u in graph[v]:
            if par[v] == u:
                continue
            par[u] = v
            depth[u] = d + 1
            stack.append(u)
    return par, depth


par, depth = dfs(0)
num = n.bit_length() + 1
doubling = [[-1] * (num) for _ in range(n)]

for i in range(n):
    doubling[i][0] = par[i]

for d in range(num - 1):
    nd = d + 1
    for i in range(n):
        if doubling[i][d] == -1:
            doubling[i][nd] = -1
        else:
            doubling[i][nd] = doubling[doubling[i][d]][d]


def query(a, b):
    def soroeru(a, b):
        if depth[a] == depth[b]:
            return a, b
        elif depth[a] < depth[b]:
            a, b = b, a
        delta = depth[a] - depth[b]
        assert delta > 0
        now = a
        for i in range(num):
            if (delta >> i) & 1:
                now = doubling[now][i]
        assert depth[now] == depth[b]
        return now, b

    a, b = soroeru(a, b)
    if a == b:
        return a
    for i in range(num)[::-1]:
        if doubling[a][i] != doubling[b][i]:
            a = doubling[a][i]
            b = doubling[b][i]
    return doubling[a][0]


for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    cc = query(c, d)
    dist = depth[d] + depth[c] - 2 * depth[cc]
    if dist % 2:
        print("Road")
    else:
        print("Town")
