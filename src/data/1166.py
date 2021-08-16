import bisect, collections, copy, heapq, itertools, math, sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    graph = [collections.deque() for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * (N + 1)
    dist[1] = 0
    stack = collections.deque([(1, 0)])
    while stack:
        r, c = stack.popleft()
        for to in graph[r]:
            if dist[to] == -1:
                dist[to] = c + 1
                stack.append((to, c + 1))
    ans = []
    for _ in range(Q):
        c, d = map(int, input().split())
        if abs(dist[c] - dist[d]) % 2 == 0:
            ans.append("Town")
        else:
            ans.append("Road")
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
