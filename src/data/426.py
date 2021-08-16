import sys

input = sys.stdin.readline

from collections import deque


def bfs(start):
    queue = deque([start])
    sign = [-1] * (n)  # 最短経路長 / 最短経路 到達可能 False
    sign[start] = 0  # 最短経路長 自分との距離は0(1往復を考えるときは消す) / 最短経路 到達可能 sign[start] = 1
    while queue:
        node = queue.popleft()  # .pop()ならdfs
        for near in nears[node]:
            if sign[near] == -1:  # 最短経路長 / 最短経路 到達可能 False
                sign[near] = sign[
                    node] + 1  # 最短経路長 / 最短経路 sign[near] = node / 到達可能 sign[near] = 1
                queue.append(near)
    return sign


n, q = [int(x) for x in input().split()]  # nは頂点の数、mは辺の数
nears = [[] for _ in range(n)]  # 隣接リスト

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    nears[a - 1].append(b - 1)
    nears[b - 1].append(a - 1)  # 有向グラフの場合は消す

d = bfs(0)
d = [0 if i % 2 == 0 else 1 for i in d]
#print(d)

for _ in range(q):
    x, y = list(map(int, input().split()))
    if abs(d[x - 1] - d[y - 1]) == 0:
        print("Town")
    else:
        print("Road")
