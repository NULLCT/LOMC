n, q = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

color = ['', 'black'] + ['?'] * (n - 1)
queue = [1]
while len(queue) != 0:
    x = queue.pop(0)
    for i in roads[x]:
        if color[i] != '?':
            continue
        if color[x] == 'black':
            color[i] = 'white'
            queue.append(i)
        else:
            color[i] = 'black'
            queue.append(i)

for _ in range(q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
