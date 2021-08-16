#再起のlimitを上げる
import sys

sys.setrecursionlimit(4100000)

n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(n - 1)]
cd = [list(map(int, input().split())) for i in range(q)]

N = n
g = [[] for _ in range(n)]
for a, b in ab:
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
visitted = [-1 for _ in range(n)]
start = 0
kyori = 0
#bfs
from collections import deque

q = deque([(start, kyori)])
while q:
    t, k = q.popleft()
    if visitted[t] == -1:
        visitted[t] = k
        for renketsu in g[t]:
            q.append((renketsu, k + 1))

# def dfs_g(cur_node,kyori,prenode=None):
#     visitted[cur_node]=kyori
#     g_renketsu = g[cur_node]
#     for c_c in g_renketsu:
#         if c_c==prenode:
#             continue
#         dfs_g(c_c,kyori+1,cur_node)
# dfs_g(start,0)

for c, d in cd:
    if abs(visitted[c - 1] - visitted[d - 1]) % 2 != 0:
        print("Road")
    else:
        print("Town")
