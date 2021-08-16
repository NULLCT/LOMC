# -*- coding: utf-8 -*-
'''
文字列取得用関数(str,int併用)
'''


def inputter(is_str=False, split=False):
    import sys
    readline = sys.stdin.readline

    if is_str:
        if split:
            return map(str, readline().rstrip().split())
        else:
            return readline().rstrip()
    else:
        if split:
            return map(int, readline().rstrip().split())
        else:
            return int(readline().rstrip())


'''
二重リストを返す関数
'''


def double_list(input_data):
    return list(list(input_data))


# G[v]: 頂点vに隣接する頂点list
# N: 頂点数
# 引用：https://tjkendev.github.io/procon-library/python/graph/bfs.html
def bfs(N, G, s):
    from collections import deque
    dist = [-1] * N
    que = deque()
    que.append(s)
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in G[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist


# main関数
def main():
    n, q = inputter(0, 1)
    G = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = inputter(0, 1)
        G[a].append(b)
        G[b].append(a)
    dist = bfs((n + 1), G, 1)
    for i in range(q):
        c, d = inputter(0, 1)
        ans = abs(dist[c] - dist[d])
        if ans % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
