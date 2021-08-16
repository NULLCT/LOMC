N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

D = [0] * N
vst = set([0])
stc = [0]
dst = [0]
while stc:
    cur = stc.pop()
    d = dst.pop()
    D[cur] = d
    for to in G[cur]:
        if to in vst:
            continue
        stc.append(to)
        dst.append(d + 1)
        vst.add(to)

ans = []
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (D[c] - D[d]) % 2:
        ans.append('Road')
    else:
        ans.append('Town')

print(*ans, sep='\n')
