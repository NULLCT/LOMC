import sys

sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
from collections import deque


def i_input():
    return int(input())


def m_input():
    return map(int, input().split())


def l_input():
    return list(map(int, input().split()))


DEBUG = False


def printd(*args):
    if DEBUG:
        print(*args)


def readinput():
    n, q = m_input()
    nList = []
    for _ in range(n):
        nList.append([])
    for _ in range(n - 1):
        a, b = m_input()
        a -= 1
        b -= 1
        nList[a].append(b)
        nList[b].append(a)
    queries = []
    for _ in range(q):
        c, d = m_input()
        queries.append((c, d))
    return n, q, nList, queries


def bfs(u, nList):
    n = len(nList)
    depth = [INFTY] * n
    visited = [False] * n
    queue = deque()
    queue.append(u)
    depth[u] = 0
    visited[u] = True
    while len(queue) > 0:
        u = queue.popleft()
        for v in nList[u]:
            if not visited[v]:
                queue.append(v)
                depth[v] = depth[u] + 1
                visited[v] = True
    return depth


def main(n, q, nList, queries):
    depth = bfs(0, nList)
    ans = []
    for c, d in queries:
        c -= 1
        d -= 1
        if abs(depth[c] - depth[d]) % 2 == 0:
            ans.append('Town')
        else:
            ans.append('Road')
    return ans


def printans(ans):
    for a in ans:
        print(a)


if __name__ == '__main__':
    n, q, nList, queries = readinput()
    ans = main(n, q, nList, queries)
    printans(ans)
