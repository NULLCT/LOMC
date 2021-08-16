import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N - 1)]
cd = [[int(i) for i in input().split()] for _ in range(Q)]
G = [[] for _ in range(N)]
for a, b in ab:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

#Euler tour
vs = [-1] * (len(G) * 2 - 1)  #DFSの訪問順
depth = [-1] * (len(G) * 2 - 1)  #根からの深さ
id = [-1] * len(G)  #各頂点がvsに初めて登場するindex
k = 0


def dfs(v, p, d):
    global k
    id[v] = k
    vs[k] = v
    depth[k] = d
    k += 1
    for i in range(len(G[v])):
        if G[v][i] != p:
            dfs(G[v][i], v, d + 1)
            vs[k] = v
            depth[k] = d
            k += 1


dfs(0, -1, 0)
for c, d in cd:
    print('Road' if (depth[id[c - 1]] - depth[id[d - 1]]) % 2 else 'Town')
