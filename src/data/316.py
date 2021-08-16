#!/usr/bin/env python3


def main():
    from collections import deque

    n, q = map(int, input().split())

    v = [[] for _ in range(n + 1)]

    for i in range(n - 1):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)

    depth_vec = [-1 for _ in range(n + 1)]

    queue = deque()
    queue.append((1, 0))

    while len(queue) > 0:
        (node, depth) = queue.pop()
        depth_vec[node] = depth

        for child in v[node]:
            if depth_vec[child] >= 0:
                continue
            queue.append((child, depth + 1))

    for i in range(q):
        c, d = map(int, input().split())
        if (depth_vec[c] + depth_vec[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


main()
