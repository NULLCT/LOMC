from collections import deque

N, Q = map(int, input().split())
AB = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    AB[a - 1].append(b - 1)
    AB[b - 1].append(a - 1)

CD = []
for i in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    CD.append([c, d])
OE = [0 for _ in range(N)]
vi = [0 for _ in range(N)]

que = deque([0])

while que:
    query = que.pop()
    for dst in AB[query]:
        if vi[dst] == 0:
            vi[dst] = 1
            OE[dst] = 1 - OE[query]
            que.append(dst)
    #print(OE)

for c, d in CD:
    if OE[c] == OE[d]:
        print("Town")
    else:
        print("Road")
