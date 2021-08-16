from collections import deque

n, q = map(int, input().split())
way = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    way[a].append(b)
    way[b].append(a)
query = []
for i in range(q):
    query.append(list(map(int, input().split())))

#n = 9
#q = 9
#way = [[], [9], [3], [2, 4, 7], [8, 5, 3], [6, 4], [5], [3], [4, 9], [8, 1]]
#query = [[7, 9], [2, 5], [2, 6], [4, 6], [2, 4], [5, 8], [7, 8], [3, 6], [5, 6]]

ans = []
dist = [-1] * (n + 1)
d = deque()

dist[1] = 0
d.append(1)

while d:
    p = d.popleft()
    for next in way[p]:
        if dist[next] != -1:
            continue
        d.append(next)
        dist[next] = dist[p] + 1

for i in range(q):
    if (dist[query[i][0]] - dist[query[i][1]]) % 2 == 0:
        print("Town")
    else:
        print("Road")
