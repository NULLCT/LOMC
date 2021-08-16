# -*- coding: utf-8 -*-
'''
文字列取得用関数(str,int併用)
'''


def inputter(is_str=False, split=False, is_list=False, loop_times=0):
    import sys
    readline = sys.stdin.readline

    return_data_list = []
    loop_cnt = loop_times
    if loop_times == 0:
        loop_cnt = 1

    for _ in range(loop_cnt):
        data = readline().rstrip()
        data_split = data.split()

        if not (split) and len(data_split) > 1:
            split = True

        if not (is_str):
            try:
                int(data_split[0])
            except:
                is_str = True

        if is_str:
            if split:
                if is_list:
                    return_data = list(list(map(str, data_split)))
                else:
                    return_data = map(str, data_split)
            else:
                if is_list:
                    return_data = list(data)
                else:
                    return_data = data
        else:
            if split:
                if is_list:
                    return_data = list(list(map(int, data_split)))
                else:
                    return_data = map(int, data_split)
            else:
                if is_list:
                    return_data = list(list(int(data)))
                else:
                    return_data = int(data)
        if loop_times != 0:
            return_data_list.append(return_data)

    if loop_times == 0:
        return return_data
    else:
        return return_data_list


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
    n, q = inputter()
    G = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = inputter()
        G[a].append(b)
        G[b].append(a)
    dist = bfs((n + 1), G, 1)
    for _ in range(q):
        c, d = inputter()
        ans = abs(dist[c] - dist[d])
        if ans % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
