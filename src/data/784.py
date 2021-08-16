import sys  #おまじない

sys.setrecursionlimit(10**6)
n, q = map(int, input().split())
road = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)


def dfs(s):  #深さ優先探索
    mile = [-1 for i in range(n)]
    mile[s] = 0  #スタート地点
    flag = [s]

    while flag:
        point = flag.pop(-1)
        nd = mile[point] + 1
        for next in road[point]:
            if mile[next] >= 0:
                continue
            mile[next] = nd
            flag.append(next)
    return mile


start = dfs(0)
for i in range(q):
    c, d = map(int, input().split())
    if abs(start[c - 1] - start[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
