import sys
from itertools import islice


def solve(in_):
    N, Q = map(int, next(in_).split())
    _graph = [[] for _ in range(N)]
    _edges = tuple(
        tuple(map(int, line.split())) for line in islice(in_, N - 1))
    queries = tuple(tuple(map(int, line.split())) for line in islice(in_, Q))

    for a, b in _edges:
        a -= 1
        b -= 1
        _graph[a].append(b)
        _graph[b].append(a)
    C = [-1] * N
    C[0] = 0
    q = [0]
    while q:
        cur = q.pop()
        for d in _graph[cur]:
            if C[d] == -1:
                C[d] = 1 - C[cur]
                q.append(d)

    ans = []
    for c, d in queries:
        c -= 1
        d -= 1

        if (C[c] + C[d]) % 2:
            ans.append('Road')
        else:
            ans.append('Town')
    return ans


def main():
    answer = solve(sys.stdin.buffer)
    print('\n'.join(answer))


if __name__ == '__main__':
    main()
