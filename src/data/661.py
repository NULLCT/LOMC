def main():
    N, Q = map(int, input().split())
    from collections import defaultdict
    d = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    ans = [0] * (1 + N)

    from collections import deque
    q = deque([1])
    visited = [False] * (1 + N)
    while q:
        t = q.popleft()
        visited[t] = True
        for nxt in d[t]:
            if visited[nxt]:
                continue
            q.append(nxt)
            ans[nxt] = 1 if ans[t] == 0 else 0

    for _ in range(Q):
        c, d = map(int, input().split())
        if ans[c] == ans[d]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
