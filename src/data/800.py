n, q = map(int, input().split())
road = [list(map(int, input().split())) for i in range(n - 1)]
queries = [list(map(int, input().split())) for i in range(q)]
edges = [[] for i in range(n + 1)]
for i in road:
    edges[i[0]].append(i[1])
    edges[i[1]].append(i[0])
stack = [1]
inf = 10**5
d = [-1 for i in range(n + 1)]
d[1] = 0
while len(stack) > 0:
    s = stack.pop()
    for i in edges[s]:
        if d[i] == -1:
            d[i] = d[s] + 1
            stack.append(i)

for i in queries:
    if abs(d[i[0]] - d[i[1]]) % 2 == 1:
        print('Road')
    else:
        print('Town')
