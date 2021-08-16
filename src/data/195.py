#まずはリストに道の状況を格納する
#その後、クエリを順に試す。

from collections import deque

N, M = map(int, input().split(' '))
list_1 = []
for i in range(N):
    list_1.append([])

# 双方向である必要はない。

for i in range(N - 1):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    list_1[a].append(b)
    list_1[b].append(a)

# 深さを記録と1を根とする根付きツリーを作成する。
depth_tree = [-1 for i in range(N)]

Q = deque()
Q.append([0, 0])

while len(Q) > 0:
    node, depth = Q.pop()
    depth_tree[node] = depth
    for c in list_1[node]:
        if depth_tree[c] >= 0:
            continue
        Q.append([c, depth + 1])

for i in range(M):
    c, d = map(int, input().split(' '))
    c -= 1
    d -= 1
    if (depth_tree[c] + depth_tree[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
