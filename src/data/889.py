###input()が遅いのでそれの対策
import sys
from collections import deque


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


###input()対策終わり
N, Q = LI()
road = []
for i in range(N - 1):
    road.append(LI())
query = []
for i in range(Q):
    query.append(LI())


##########
def bfs(graph, start):
    arrive = [-1 for _ in range(N + 1)]
    stack = deque()
    stack.append(start)
    arrive[start] = 0
    while stack:
        target = stack.popleft()
        for i in graph[target]:
            if arrive[i] != -1:
                continue
            else:
                arrive[i] = arrive[target] + 1
                stack.append(i)
    return arrive


graph = [deque([]) for _ in range(N + 1)]

for i in range(N - 1):
    s, g = road[i]
    graph[g].append(s)
    graph[s].append(g)

##########
##木の直系を求める
result = bfs(graph, 1)
#print(result)
edge = result.index(max(result))

finalmap = bfs(graph, edge)
###########

for i in range(Q):
    start, goal = query[i]
    start_pos = finalmap[start]
    goal_pos = finalmap[goal]

    if (start_pos - goal_pos) % 2 == 0:
        print("Town")
    else:
        print("Road")
