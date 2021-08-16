import sys

sys.setrecursionlimit(10000000)

N, Q = map(int, input().split())

neighbor = {}
visited = [-1]
for i in range(N - 1):
    tmpA, tmpB = map(int, input().split())
    if tmpA - 1 not in neighbor.keys():
        neighbor[tmpA - 1] = []
    if tmpB - 1 not in neighbor.keys():
        neighbor[tmpB - 1] = []
    neighbor[tmpA - 1].append(tmpB - 1)
    neighbor[tmpB - 1].append(tmpA - 1)
    visited.append(-1)

#print(neighbor)
#print(visited)


def dfs(pos, flg):
    #print(pos, visited[pos])
    visited[pos] = flg
    for i in neighbor[pos]:
        #print(i, visited[i])
        if visited[i] == -1:
            dfs(i, 1 - flg)


dfs(0, 0)

#print(visited)

for i in range(Q):
    tmpC, tmpD = map(int, input().split())
    if visited[tmpC - 1] == visited[tmpD - 1]:
        print("Town")
    else:
        print("Road")

#print(visited)
