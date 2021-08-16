import sys
import collections

sys.setrecursionlimit(10**8)

input = sys.stdin.readline


def main():
    N, Q = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(N - 1)]
    CD = [[int(x) for x in input().split()] for _ in range(Q)]

    edge = [[] for j in range(N)]

    for a, b in AB:
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    ans = [-1] * N
    ans[0] = 0

    q = collections.deque()
    q.append([0, 0])
    visited = set()
    visited.add(0)

    while q:
        c, cc = q.pop()
        next_color = (cc + 1) % 2

        for next in edge[c]:
            if next not in visited:
                visited.add(next)
                ans[next] = next_color
                q.append([next, next_color])

    for c, d in CD:
        c -= 1
        d -= 1
        if ans[c] == ans[d]:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
