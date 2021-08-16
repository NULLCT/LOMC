N, Q = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N - 1)]
cd = [[int(i) for i in input().split()] for _ in range(Q)]

vec = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    vec[a].append(b)
    vec[b].append(a)

q = [0]
p = [-1] * N
while q:
    cur = q.pop()
    cp = p[cur]
    for nex in vec[cur]:
        if p[nex] != -1:
            continue

        q.append(nex)
        p[nex] = 1 - cp

for c, d in cd:
    c -= 1
    d -= 1
    if p[c] == p[d]:
        print('Town')
    else:
        print('Road')
