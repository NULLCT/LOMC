#
# abc209 d
#
import sys
from io import StringIO
import unittest
import collections


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 1
1 2
2 3
2 4
1 2"""
        output = """Road"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 2
2 3
3 4
4 5
1 3
1 5"""
        output = """Town
Town"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 9
2 3
5 6
4 8
8 9
4 5
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
5 6"""
        output = """Town
Road
Town
Town
Town
Town
Road
Road
Road"""
        self.assertIO(input, output)


def resolve():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    D = [-1] * N
    q = collections.deque()
    D[0] = 0
    q.append(0)
    while q:
        p = q.popleft()
        for np in G[p]:
            if D[np] != -1:
                continue
            D[np] = D[p] + 1
            q.append(np)

    for c, d in CD:
        if abs(D[c - 1] - D[d - 1]) % 2:
            print("Road")
        else:
            print("Town")


if __name__ == "__main__":
    # unittest.main()
    resolve()
