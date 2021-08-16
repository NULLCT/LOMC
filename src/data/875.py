import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
import array as ar

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N - 1)]
CD = [list(map(int, input().split())) for i in range(Q)]

g = defaultdict(list)
for a, b in AB:
    g[a].append(b)
    g[b].append(a)

depth = [0] * (N + 1)
parent = [1] * (N + 1)
visited = [False] * (N + 1)
dq = deque([1])
while dq:
    v = dq.popleft()
    visited[v] = True
    for nv in g[v]:
        if visited[nv]:
            continue
        depth[nv] = depth[v] + 1
        parent[nv] = v
        dq.append(nv)

anc = [ar.array('I', list(range(N + 1))), ar.array('I', parent)]
for i in range(15):
    temp = ar.array('I', [1] * (N + 1))
    for v in range(1, N + 1):
        temp[v] = anc[-1][anc[-1][v]]
    anc.append(temp)

for c, d in CD:
    tc, td = c, d
    while tc != td:
        for i in range(len(anc) - 1, -1, -1):
            if anc[i][tc] != anc[i][td]:
                tc = anc[i][tc]
                td = anc[i][td]
        if parent[tc] == parent[td]:
            break
    a = parent[tc]
    d = depth[c] + depth[d] - 2 * depth[a]
    if d % 2 == 0:
        print('Town')
    else:
        print('Road')
