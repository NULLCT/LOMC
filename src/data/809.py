from collections import deque


def bfs(c, d):
    queue = deque([c])
    dis[c] = 0
    while queue:
        # print(queue)
        v = queue.popleft()
        for i in road[v]:
            if dis[i] == None:
                queue.append(i)
                dis[i] = dis[v] + 1
                # road[v].remove(i)


n, q = map(int, input().split())
road = [[] for _ in range(n)]
for i in range(n - 1):
    ab = list(map(int, input().split()))
    road[ab[0] - 1].append(ab[1] - 1)
    road[ab[1] - 1].append(ab[0] - 1)
ans = []
# print(road)
dis = [None] * n
bfs(0, n)
# print(dis)
for i in range(q):
    cd = list(map(int, input().split()))
    c = cd[0] - 1
    d = cd[1] - 1
    if (dis[c] + dis[d]) % 2 != 0:
        ans.append(True)
    else:
        ans.append(False)
for i in ans:
    if i:
        print("Road")
    else:
        print("Town")
