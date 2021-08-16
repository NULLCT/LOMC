from collections import deque

n, q = map(int, input().split())
road = dict()
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a in road:
        road[a].append(b)
    else:
        road[a] = [b]

    if b in road:
        road[b].append(a)
    else:
        road[b] = [a]

visted = [False] * n
visted[0] = True
queue = deque()
color = [""] * n
color[0] = 'b'
queue.append(0)
while queue:
    town = queue.popleft()
    for des in road[town]:
        if visted[des] is False:
            if color[town] == 'b':
                color[des] = 'r'
                queue.append(des)
                visted[des] = True
            else:
                color[des] = 'b'
                queue.append(des)
                visted[des] = True
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
