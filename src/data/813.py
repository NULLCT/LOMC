from collections import deque
import sys

sys.setrecursionlimit(500000)
#入力が
#頂点数　辺数
#辺iの始点　終点 for i in range(辺数)
#だったとして
n, q = map(int, input().split())
g = [[] for i in range(n)]  #g[i]はグラフの頂点iに隣接する頂点（有向）
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

seen = [False] * n  #seen[i]は頂点iが検知済みか
todo = deque()  #todoは検知したが訪問済みでない頂点のリスト
parity = [-1] * n


#ここからDFS
def dfs(s):
    seen[s] = True
    todo.append(s)
    #処理とか
    while todo:
        v = todo.pop()
        for i in g[v]:
            if seen[i] == True:
                continue
            parity[i] = (parity[v] + 1) % 2
            dfs(i)


parity[0] = 0
dfs(0)

for j in range(q):
    c, d = map(int, input().split())
    if parity[c - 1] == parity[d - 1]:
        print("Town")
    else:
        print("Road")
