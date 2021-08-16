#abc209_d
import sys, math, collections, itertools, heapq, functools, bisect

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
m = 10**9 + 7


def intm1(num):
    return int(num) - 1


intfunc = [int, intm1]


def II(i=0):
    return intfunc[i](input())


def LII(i=0):
    return list(map(intfunc[i], input().split()))


def SI():
    return input().rstrip()


def LSI():
    return list(input().rstrip().split())


inf = float("inf")


def yes():
    return print("Yes")


def no():
    return print("No")


#abc209_d

N, Q = LII()
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = LII(1)
    edge[a].append(b)
    edge[b].append(a)

point = [inf] * N
point[0] = 0
q = collections.deque()
q.append(0)
while q:
    now = q.popleft()
    for ed in edge[now]:
        if point[ed] > point[now] + 1:
            q.append(ed)
            point[ed] = point[now] + 1

for _ in range(Q):
    a, b = LII(1)
    c = abs(point[a] - point[b])
    if c % 2 == 0:
        print("Town")
    else:
        print("Road")
