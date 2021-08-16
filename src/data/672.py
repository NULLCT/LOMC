# coding: utf-8
import sys
import math
import io
from collections import Counter
from collections import deque


def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(i_map())


def main():
    n, q = i_map()
    global R
    R = [[] for _ in range(n + 1)]
    global color
    color = [0 for _ in range(n + 1)]
    color[1] = 1

    for _ in range(n - 1):
        a, b = i_map()
        R[a].append(b)
        R[b].append(a)

    #dfs(1)
    que = deque()

    que.append(1)

    while que:
        t = que.popleft()
        for r in R[t]:
            if color[r] == 0:
                color[r] = color[t] * -1
                que.append(r)

    for i in range(q):
        c, d = i_map()
        if color[c] == color[d]:
            print("Town")
        else:
            print("Road")


def dfs(s):
    for r in R[s]:
        if color[r] == 0:
            color[r] = color[s] * -1
            dfs(r)


if __name__ == '__main__':
    _INPUT = '''\
4 1
1 2
2 3
2 4
1 2


    '''
    if sys.platform == 'win32':
        sys.stdin = io.StringIO(_INPUT)

    main()
