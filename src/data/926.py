from collections import defaultdict, Counter, deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

A = [0 for _ in range(N)]

st = 0
for i in range(N):
    if len(G[i]) == 1:
        st = i
        break

d = deque([st])
al = set([st])
turn = 0
while d:
    #print(d)
    turn += 1
    for _ in range(len(d)):
        q = d.popleft()
        for i in range(len(G[q])):
            nex = G[q][i]
            if nex in al:
                continue
            d.append(nex)
            al.add(nex)
            A[nex] = turn

for _ in range(Q):
    c, d = map(int, input().split())
    ans = abs(A[d - 1] - A[c - 1])
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
