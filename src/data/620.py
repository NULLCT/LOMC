from collections import deque

n, m = map(int, input().split())
lis = [[] for i in range(n)]
lis.append([])

for i in range(n - 1):
    a, b = map(int, input().split())  #aとbが辺で結ばれている
    a -= 1
    b -= 1
    lis[a].append(b)
    lis[b].append(a)

dis = [-1 for i in range(n)]
dis[0] = 0
que = deque([0])

while que:
    q = que.popleft()
    for node in lis[q]:
        if dis[node] != -1:
            continue
        dis[node] = (dis[q] + 1) % 2
        que.append(node)

for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dis[c] == dis[d]:
        print("Town")
    else:
        print("Road")
