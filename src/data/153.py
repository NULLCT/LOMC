def main():
    import sys
    sys.setrecursionlimit(10**7)
    from collections import deque

    def input():
        return sys.stdin.readline()[:-1]

    n, q = map(int, input().split())
    road = [[] for _ in range(n)]

    for i in range(n - 1):
        a, b = map(int, input().split())
        road[a - 1].append(b - 1)
        road[b - 1].append(a - 1)

    d = deque()
    d.append(0)
    dist = [-1] * n
    dist[0] = 0

    while d:
        v = d.popleft()
        for i in road[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    for i in range(q):
        c, d = map(int, input().split())
        if (dist[c - 1] - dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
