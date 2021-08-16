from collections import deque
import numpy as np


def bfs(start, links):
    queue = deque()
    queue.append((start, 0))
    ans = [None for _ in range(len(links))]
    while len(queue) > 0:
        cur, distance = queue.popleft()
        if ans[cur] is not None:
            continue
        ans[cur] = distance
        candidates = [(place, distance + 1) for place in links[cur]
                      if ans[place] is None]
        queue.extend(candidates)

    return ans


n, q = map(int, input().split())
links = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)

temp_distances = bfs(0, links)
start = np.argmax(temp_distances)

distances = bfs(start, links)

for _ in range(q):
    c, d = map(int, input().split())
    if (distances[c - 1] - distances[d - 1]) % 2 != 0:
        print("Road")
    else:
        print("Town")
