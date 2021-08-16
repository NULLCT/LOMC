import sys

MAXX = 10**7 + 20
sys.setrecursionlimit(MAXX)
#input = sys.stdin.readline

N, Q = map(int, input().split())
adj = [[] for _ in range(N + 3)]
for i in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
#print(adj)
#label = []
lvl = []
id = [0] * (N + 2)
count = 0


def dfs(v, parent, depth):
    global count
    if depth > N + 10:
        return

    count += 1
    #label.append(v)
    lvl.append(depth)
    if id[v] <= 0:
        id[v] = count
    for u in adj[v]:
        if u == parent: continue
        dfs(u, v, depth + 1)
        #count += 1
        #label.append(v)
        #lvl.append(depth)


dfs(N // 2, 0, 0)
#print(id)
#print(lvl)
ans = []
for _ in range(Q):
    u, v = map(int, input().split())
    ll, rr = id[u] - 1, id[v] - 1  #ノードIDから訪れる順に変換
    dist = lvl[ll] + lvl[rr]  #- 2*lvl[id[lca]-1]
    if dist & 0x01 == 0:
        print('Town')
        #ans.append('Town')
    else:
        print('Road')
        #ans.append('Road')
