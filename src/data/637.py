import collections

n, q = list(map(int, input().split()))

queries = []
mp = collections.defaultdict(list)

for i in range(n + q - 1):
    a, b = list(map(int, input().split()))
    if i < n - 1:

        mp[a].append(b)
        mp[b].append(a)
    else:
        queries.append([a, b])

dist = [-1 for i in range(n + 1)]


def bfs(node):

    vis = [0 for i in range(n + 1)]
    queue = collections.deque()

    queue.append(node)
    vis[node] = 1
    dist[node] = 0
    level = 1
    while len(queue) > 0:
        curr_node = queue.popleft()
        for child in mp[curr_node]:
            if not vis[child]:
                queue.append(child)
                vis[child] = 1
                dist[child] = 1 - dist[curr_node]
        level += 1


bfs(1)
# print(dist)

for c, d in queries:
    # c,d = list(map(int, input().split()))
    # print(f"from {c} to {d} : {dist[c] - dist[d]}")
    if dist[c] == dist[d]:
        print("Town")
    else:
        print("Road")
