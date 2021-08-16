import sys

sys.setrecursionlimit(1000000)


def dfs(n, graph, parent, dists, dist):
    for i in graph[n]:
        if parent == i:
            continue
        dists[i] = dist
        dfs(i, graph, n, dists, dist + 1)


def main():
    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dists = [-1 for _ in range(n)]
    dists[0] = 0

    dfs(0, graph, -1, dists, 1)

    for _ in range(q):
        c, d = map(int, input().split())
        print("Road" if (dists[c - 1] + dists[d - 1]) % 2 else "Town")


if __name__ == "__main__":
    main()
