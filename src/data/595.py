from collections import deque

N, Q = map(int, input().split())
INF = float('INF')
edge = [[] for n in range(N)]
for n in range(N - 1):
    a, b = map(int, input().split())
    #print(a,b)
    edge[a - 1] += [b - 1]
    edge[b - 1] += [a - 1]
#for e in edge:
#    print(e)

townColor = [-1 for n in range(N)]
townColor[0] = 0
#print(townColor)
d = deque([0])
while d:
    mypos = d.popleft()
    for i in edge[mypos]:
        if townColor[i] == -1:
            d.append(i)
            townColor[i] = townColor[mypos] + 1
#print(townColor)
for q in range(Q):
    c, d = map(int, input().split())
    if townColor[c - 1] % 2 == townColor[d - 1] % 2:
        print('Town')
    else:
        print('Road')
