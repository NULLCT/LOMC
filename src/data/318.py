N, Q = map(int, input().split())
root = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    root[a - 1].append(b - 1)
    root[b - 1].append(a - 1)
ischecked = [-1] * N
q = [0]
ischecked[0] = 0
while q:
    now = q.pop()
    dist = (ischecked[now] + 1) % 2
    for nex in root[now]:
        if ischecked[nex] >= 0:
            continue
        ischecked[nex] = dist
        q.append(nex)
for _ in range(Q):
    c, d = map(int, input().split())
    if ischecked[c - 1] == ischecked[d - 1]:
        print("Town")
    else:
        print("Road")
