# d
import queue

n, q = map(int, input().split())
ablist = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    ablist[a - 1].append(b - 1)
    ablist[b - 1].append(a - 1)

cdlist = []
for _ in range(q):
    c, d = map(int, input().split())
    cdlist.append([c - 1, d - 1])

# print(ablist)
# print(cdlist)
# n = 4
# q = 1
# ablist = [[1], [0, 2, 3], [1], [1]]
# cdlist = [[0, 1]]

que = queue.Queue()
color = [-1] * n
color[0] = 0  # 最初は色0
que.put(0)  # 探索リストはインデックス0から始める

while not que.empty():
    t = que.get()
    for i in ablist[t]:
        if color[i] == -1:
            # 今の色が0なら1、1なら0になる（この式こうなるのか）
            color[i] = 1 - color[t]
            # 探索すべきリストに今の街からつながってる街を加える（幅優先探索）
            que.put(i)

for c, d in cdlist:
    if color[c] == color[d]:
        ans = "Town"
    else:
        ans = "Road"
    print(ans)
