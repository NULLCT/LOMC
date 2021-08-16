def main():
    from collections import deque
    N, Q = map(int, input().split())
    ab = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        ab[a - 1].append(b - 1)
        ab[b - 1].append(a - 1)

    def bfs(s):
        q = deque([s])
        D = [-1] * N
        D[s] = 0
        while q:
            v = q.popleft()
            for i in ab[v]:
                if D[i] == -1:
                    D[i] = D[v] + 1
                    q.append(i)
        return D

    D = bfs(0)

    for _ in range(Q):
        c, d = map(int, input().split())
        if (D[c - 1] - D[d - 1]) % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
