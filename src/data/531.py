"""
解説見た
めっちゃ惜しいところまで行ってた
考察結果(計算量の推定，dfs使う，偶奇判定)は全部正解

肝は各nodeと隣り合うnodeを区別して(0, 1を割り振る)同じ番号かどうか(つまり偶奇判定は惜しかった)
で各クエリにO(1)で解答できる

くっっっっっそおしいやんけ
"""

from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
Graph = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)


def bfs(start_pos: int) -> list:
    marked = [1 if idx == start_pos else 0 for idx in range(n)]
    nexts = deque([start_pos])
    while nexts:
        now = nexts.popleft()
        for now_pos in Graph[now]:
            if marked[now_pos] == 0:
                marked[now_pos] = -marked[now]
                nexts.append(now_pos)
    return marked


Marked: list = bfs(0)
ans = ["" for _ in range(q)]
for query in range(q):
    c, d = map(int, input().split())
    if Marked[c - 1] == Marked[d - 1]:
        ans[query] = "Town"
    else:
        ans[query] = "Road"

for a in ans:
    print(a)
