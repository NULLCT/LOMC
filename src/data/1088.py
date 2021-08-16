from collections import deque


def main():
    n, q = map(int, input().split())

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        adj[a].append(b)
        adj[b].append(a)

    queue = deque()
    queue.append(0)
    dist = [-1 for _ in range(n)]
    dist[0] = 0

    while queue:
        now_v = queue.popleft()
        for next_v in adj[now_v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[now_v] + 1
            queue.append(next_v)

    for _ in range(q):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        if abs(dist[d] - dist[c]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
