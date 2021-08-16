import sys

sys.setrecursionlimit(10**7)
N, Q = map(int, input().split())
es = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    es[a - 1].append(b - 1)
    es[b - 1].append(a - 1)

colors = [0 for i in range(N)]


def dfs(v, color):
    #今いる点を着色
    colors[v] = color
    #今の頂点から行けるところをチェック
    for to in es[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    #調べ終わったら矛盾がないのでTrue
    return colors


z = dfs(0, 1)

for i in range(Q):
    c, d = map(int, input().split())
    if z[c - 1] == z[d - 1]:
        print('Town')
    else:
        print('Road')
