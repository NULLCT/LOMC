from collections import deque
import sys


def bfs(T, n, D):
    D[1] = 0
    q = deque([1])
    while q:
        c = q.popleft()
        for i in T[c]:
            if D[i] == n:
                D[i] = D[c] + 1
                q.append(i)


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    T = [[] for i in range(n + 1)]
    D = [n] * (n + 1)
    for i in range(1, n):
        a, b = map(int, input().split())
        T[a].append(b)
        T[b].append(a)
    bfs(T, n, D)
    for _ in range(q):
        c, d = map(int, input().split())
        if (D[c] + D[d]) % 2 == 1:
            print('Road')
        else:
            print('Town')


main()
