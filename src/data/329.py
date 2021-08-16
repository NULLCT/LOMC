from collections import deque


#1.クラスを宣言：
class Node:
    # コンストラクタを宣言
    def __init__(self, index):
        # メソッドを定義
        self.index = index  # Node （頂点） の番号を定義
        self.nears = []  # 隣接 Node のリストを定義
        self.sign = -1  # 未探索の場合は -1 を返す。探索済みの場合、

    def __repr__(self):
        return f'Node index:{self.index} Node nears:{self.nears} Node sign:{self.sign}'


# 入力読み込み
N, Q = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

#2.インスタンス（Node）を生成し、nodes に格納する:
# ノード 0 も生成されるが使用しない。
nodes = []
for i in range(N + 1):
    nodes.append(Node(i))

# この時点で探索済みの node は存在しないため sign メソッドで -1 が返される。
#print([node.sign for node in nodes])

#3.隣接 node を nears メソッドに格納する:
for j in range(N - 1):
    edge_start, edge_end = links[j]
    nodes[edge_start].nears.append(edge_end)
    nodes[edge_end].nears.append(edge_start)  # 有向グラフの場合は消す（無向グラフの場合のみ記述）

# BFS
# 探索対象 node を queue （キュー）に入れる。
queue = deque()
#5-1.本問では node 1 から探索を開始するため queue に node 1 を最初に入れる:
queue.append(nodes[1])

#5-2.queue がなくなるまで探索を続ける:
while queue:
    #5-2-1.queue から node を 1 つ取り出す。取り出したノードについて調べる。
    # 取り出された node は queue から消える。
    node = queue.popleft()  # .pop() にすると DFS になる
    #print(node) # コメントアウトを外すと現在地がわかる。 DFS と BFS で比べてみるとよい
    #5-2-2.取り出された node の隣接 node 達を nears に入れる。
    nears = node.nears
    #5-2-3.隣接 node 達が探索済みか 1 つずつ調べる。
    for near in nears:
        #5-2-4.未探索の隣接 node は queue に追加する。
        # 取り出してきた親 node は道しるべとなるため、子 node の sign メソッドに追加する。
        if nodes[near].sign == -1:
            queue.append(nodes[near])
            nodes[near].sign = node.sign + 1

# 道しるべを表示
for k in range(2, N + 1):
    nodes[k].sign
for i in range(Q):
    if (nodes[CD[i][0]].sign - nodes[CD[i][1]].sign) % 2 == 0:
        print("Town")
    else:
        print("Road")
