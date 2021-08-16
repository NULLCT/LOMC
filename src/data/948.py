import sys
from io import StringIO
import unittest
from collections import deque

INF = float('inf')


def resolve():
    n, q = list(map(int, input().split()))
    d = {}
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        if a not in d:
            d[a] = []
        d[a].append(b)
        if b not in d:
            d[b] = []
        d[b].append(a)

    result = {}
    for i in range(n):
        result[i] = -1

    depth = 0
    queue = deque()
    queue.appendleft((0, 0))
    while queue:
        index, depth = queue.pop()
        if result[index] != -1:
            continue
        result[index] = depth

        for child in d[index]:
            queue.appendleft((child, depth + 1))

    # print(result)

    for _ in range(q):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        if (result[c] + result[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


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


if __name__ == "__main__":
    # unittest.main()
    resolve()
