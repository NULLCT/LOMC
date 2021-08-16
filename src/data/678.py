def bfs(s):
    col = 0
    q = [s]
    ch[s] = col
    while q != []:
        f = q[0]
        col = ch[f]
        for u in mat[f]:
            if ch[u] == None:
                ch[u] = 1 - col
                q.append(u)
        q.pop(0)


N, Q = list(map(int, input().split()))
mat = [[] for _ in range(N + 1)]
ch = [None for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    mat[a].append(b)
    mat[b].append(a)

bfs(1)

for _ in range(Q):
    c, d = list(map(int, input().split()))
    if ch[c] == ch[d]:
        print("Town")
    else:
        print("Road")
