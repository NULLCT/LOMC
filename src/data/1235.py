from collections import deque
import sys

input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    fr = 0
    que = deque([fr])
    goneset = set([fr])
    count = [0] * N
    while True:
        fr = que.popleft()
        for to in graph[fr]:
            if to in goneset:
                continue
            count[to] = count[fr] + 1
            que.append(to)
            goneset.add(to)
        if len(que) == 0:
            break

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if count[c] % 2 == count[d] % 2: print('Town')
        else: print('Road')


if __name__ == "__main__":
    main()
