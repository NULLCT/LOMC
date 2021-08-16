def main():
    from collections import deque, defaultdict
    n, query = map(int, input().split())
    tree = defaultdict(list)
    q = deque([1])
    vis = [0] * (n + 1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    while q:
        length = len(q)
        s = set()
        for _ in range(length):
            node = q.popleft()
            vis[node] = 1
            for son in tree[node]:
                dist[son] = min(dist[son], dist[node] + 1)
                if vis[son] == 0:
                    q.append(son)

    for _ in range(query):
        c, d = map(int, input().split())
        res = 'Road'
        if dist[c] % 2 == dist[d] % 2:
            res = 'Town'
        print(res)

    return


main()