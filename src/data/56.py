n, q = map(int, input().split())
map_list = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    map_list[a].append(b)
    map_list[b].append(a)

que = [0]
done = [None] * n
done[0] = 1

for v in que:
    for to in map_list[v]:
        if done[to] is None:
            done[to] = done[v] + 1
            que.append(to)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (done[c] + done[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
