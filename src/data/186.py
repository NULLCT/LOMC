N, Q = map(int, input().split())
CHECKED = [-1 for i in range(N + 1)]
ROOT = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    ROOT[a].append(b)
    ROOT[b].append(a)

queue = [1]
CHECKED[1] = 0

#幅優先探索
while not queue == []:
    now = queue.pop(0)
    for n in ROOT[now]:
        if CHECKED[n] == -1:
            CHECKED[n] = CHECKED[now] + 1
            queue.append(n)

cd = []

for j in range(Q):
    c, d = map(int, input().split())
    cd.append([c, d])

for k in cd:
    if (CHECKED[k[0]] - CHECKED[k[1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
