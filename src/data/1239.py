import sys

sys.setrecursionlimit(10000000)


def dfs(a):
    for i in load[a]:
        if length[i] != -1:
            continue
        else:
            length[i] = length[a] + 1
            dfs(i)
    return


n, q = map(int, input().split())
length = [-1 for i in range(n + 1)]
length[1] = 0
load = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    load[a].append(b)
    load[b].append(a)
dfs(1)
for i in range(q):
    c, d = map(int, input().split())
    if (length[c] - length[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
