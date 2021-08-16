import sys
#from numba import jit
#import collections
#import math
#sys.setrecursionlimit(200000)

input_methods = ['clipboard', 'file', 'key']
using_method = 0
input_method = input_methods[using_method]

tin = lambda: map(int, input().split())
lin = lambda: list(tin())
MOD = 1000000007
INF = 10**12

#+++++
#for copy from lib

#+++++


def main():
    #n = int(input())
    n, q = tin()
    #s=input()
    #al=lin()
    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = tin()
        path[a - 1].append(b - 1)
        path[b - 1].append(a - 1)
    dist = [-1] * n
    dist[0] = 0
    pp = []
    for np in path[0]:
        pp.append(np)
        dist[np] = 1

    while len(pp) > 0:
        np = pp[-1]
        pp.pop()
        for nnp in path[np]:
            if dist[nnp] != -1:
                continue
            dist[nnp] = dist[np] + 1
            pp.append(nnp)

    for _ in range(q):
        a, b = tin()
        a, b = a - 1, b - 1
        dd = dist[a] + dist[b]
        if dd % 2 == 0:
            print('Town')
        else:
            print('Road')


#+++++
isTest = False


def pa(*vl):
    if not isTest:
        return
    #for v in vl:
    print(vl)


def input_clipboard():
    import clipboard
    input_text = clipboard.get()
    input_l = input_text.splitlines()
    for l in input_l:
        yield l


if __name__ == "__main__":
    if sys.platform == 'ios':
        if input_method == input_methods[0]:
            ic = input_clipboard()
            input = lambda: ic.__next__()
        elif input_method == input_methods[1]:
            sys.stdin = open('inputFile.txt')
        else:
            pass
        isTest = True
    else:
        pass
        #input = sys.stdin.readline

    ret = main()
    if ret is not None:
        print(ret)
