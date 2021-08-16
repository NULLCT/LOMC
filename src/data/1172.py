from collections import deque


def main():
    N, Q = map(int, input().split())
    G = [set() for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].add(b - 1)
        G[b - 1].add(a - 1)

    depth = [-1] * N
    depth[0] = 0

    que = deque([0])

    while que:
        v = que.pop()
        d = depth[v]
        for nv in G[v]:
            if depth[nv] != -1: continue
            depth[nv] = d + 1
            que.append(nv)

    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    R = ['Town', 'Road']

    for c, d in query:
        if (depth[c - 1] - depth[d - 1]) % 2 == 0:
            ans.append(0)
        else:
            ans.append(1)

    for a in ans:
        print(R[a])


if __name__ == '__main__':
    main()
