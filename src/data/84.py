N, Q = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(N - 1)]
a = [i[0] for i in tmp]
b = [i[1] for i in tmp]
tmp = [list(map(int, input().split())) for _ in range(Q)]
c = [i[0] for i in tmp]
d = [i[1] for i in tmp]
l = []
for i in range(N):
    l.append([])
for i in range(N - 1):
    l[a[i] - 1].append(b[i] - 1)
    l[b[i] - 1].append(a[i] - 1)
D = {}
D[0] = 0
q = [0]
while q != []:
    u = q.pop()
    for i in l[u]:
        if i not in D:
            D[i] = D[u] + 1
            q.append(i)
for i in range(Q):
    if (D[c[i] - 1] + D[d[i] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
