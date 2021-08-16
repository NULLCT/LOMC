import numpy as np
import queue


def stdin_input():
    N, Q = map(int, input().split())
    a, b = [], []
    for i in range(N - 1):
        line = input()
        a.append(int(line.split()[0]) - 1)
        b.append(int(line.split()[1]) - 1)
    c, d = [], []
    for i in range(Q):
        line = input()
        c.append(int(line.split()[0]) - 1)
        d.append(int(line.split()[1]) - 1)
    return N, Q, a, b, c, d


def fixed_input():
    input_text = '''9 9
8 9
2 3
4 8
4 5
5 6
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6
'''
    lines = input_text.splitlines()
    N, Q = map(int, lines[0].split())
    a, b = [], []
    for i in range(N - 1):
        a.append(int(lines[1 + i].split()[0]) - 1)
        b.append(int(lines[1 + i].split()[1]) - 1)
    c, d = [], []
    for i in range(Q):
        c.append(int(lines[N + i].split()[0]) - 1)
        d.append(int(lines[N + i].split()[1]) - 1)
    return N, Q, a, b, c, d


def get_distance_from_0(N, a, b):
    #paths = sorted([(min(a[i], b[i]), max(a[i], b[i])) for i in range(N-1)])
    # destination = [[] for i in range(N)]
    # for i in range(N-1):
    #   destination[a[i]].append(b[i])
    #   destination[b[i]].append(a[i])
    # dist = np.zeros(N, dtype=int)
    # for path in paths:
    #   dist[path[1]] = dist[path[0]] + 1
    # return dist

    dist = [-1 for i in range(N)]
    dist[0] = 0
    destination = [[] for i in range(N)]
    for i in range(N - 1):
        destination[a[i]].append(b[i])
        destination[b[i]].append(a[i])
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        i = q.get()
        for j in destination[i]:
            if dist[j] >= 0:
                continue
            q.put(j)
            dist[j] = dist[i] + 1
    return dist


def is_meet_town(in_obj):
    N, Q, a, b, c, d = in_obj
    d0 = get_distance_from_0(N, a, b)
    results = []
    for i in range(Q):
        results.append((d0[c[i]] + d0[d[i]]) % 2 == 0)
    return results


def show_result(out_obj):
    for result in out_obj:
        print("Town" if result else "Road")


#in_obj = fixed_input()
in_obj = stdin_input()
out_obj = is_meet_town(in_obj)
show_result(out_obj)
