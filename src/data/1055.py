from collections import deque


def main():
    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dists = [-1 for _ in range(n)]
    dists[0] = 0

    reached = [False for _ in range(n)]

    d = deque()
    d.append(0)
    reached[0] = True

    for _ in range(n):
        v = d.pop()
        for i in graph[v]:
            if reached[i]:
                continue
            dists[i] = dists[v] + 1
            reached[i] = True
            d.append(i)
        if not d:
            break

    for _ in range(q):
        c, d = map(int, input().split())
        print("Road" if (dists[c - 1] + dists[d - 1]) % 2 else "Town")


if __name__ == "__main__":
    main()
