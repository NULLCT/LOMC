import sys
from collections import deque

sys.setrecursionlimit(10**6)


def main(input, print):
    n, q = map(int, input().split())
    table = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        table[a].append(b)
        table[b].append(a)
    color = [-1] * n
    color[0] = 0
    que = deque()
    que.append(0)
    while que:
        now = que.popleft()
        for next in table[now]:
            if color[next] == -1:
                color[next] = 1 - color[now]
                que.append(next)
    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (color[c] == color[d]):
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main(sys.stdin.readline, print)
