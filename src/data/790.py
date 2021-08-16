from collections import deque
import copy

n, q = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
INF = pow(10, 9) + 7

# dp = [[INF,set()] for i in range(n)]
# dp[0] = [0,{0}]
# def dijkstra(s,p):
#     # dp = [[INF,set()]]*n
#     d = deque()
#     d.append((s, 0, p))
#     while(d):
#         v,cost,p = d.popleft()
#         # if(dp[v][0] <= cost): continue
#         dp[v][0] = cost
#         if(p!=-1): dp[v][1] = copy.deepcopy(dp[p][1])
#         dp[v][1].add(v)

#         # if(v == g): return dp[g][0]
#         for to in G[v]:
#             if(dp[to][0] <= cost+1): continue
#             # if(to == v): continue
#             d.append((to, cost+1, v))

# dijkstra(0, -1)

d = deque()
d.append(0)
dp = [-1] * n
dp[0] = 0
while (d):
    v = d.popleft()
    for to in G[v]:
        if (dp[to] != -1): continue
        dp[to] = 1 - dp[v]
        d.append(to)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dp[c] == dp[d]): print('Town')
    else: print('Road')
