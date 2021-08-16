import math
import sys

sys.setrecursionlimit(100000000)


def main():
    inf = math.inf
    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1  # 0-indexed
        graph[a].append(b)
        graph[b].append(a)

    depth = [-1 for _ in range(n)]
    start = 0
    visited = [False for _ in range(n)]
    make_depth(depth, graph, start, visited, 0)

    for j in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        c_depth = depth[c]
        d_depth = depth[d]
        if abs(c_depth - d_depth) % 2 == 0:
            answer = "Town"
        else:
            answer = "Road"
        print(answer)


def make_depth(depth_lst, graph, here, visited, depth=0):
    depth_lst[here] = depth
    visited[here] = True

    for nxt in graph[here]:
        if visited[nxt]:
            continue
        make_depth(depth_lst, graph, nxt, visited, depth + 1)


if __name__ == '__main__':
    main()
