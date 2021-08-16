N, Q = map(int, input().split(' '))

visited = [0] * N
edges = [set() for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split(' '))
    edges[a - 1].add(b - 1)
    edges[b - 1].add(a - 1)

search = set([0])
visited[0] = 1
flag = 1

while True:
    flag *= -1
    nsearch = set()
    while len(search):
        a = search.pop()
        for p in edges[a]:
            if visited[p] == 0:
                visited[p] = flag
                nsearch.add(p)
    if nsearch == set():
        break
    search = nsearch

for i in range(Q):
    c, d = map(int, input().split(' '))
    result = visited[c - 1] * visited[d - 1]
    if result == 1:
        print('Town')
    else:
        print('Road')
