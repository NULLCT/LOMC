import sys
from sys import stdin
#import numba as nb
#from numba import b1, i4, i8, f8
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq
#import networkx as nx
from itertools import combinations, permutations
import math
#import numpy as np


def main(n, q, ab, cd):
    dic = {i: set() for i in range(1, n + 1)}
    for i in range(n - 1):
        dic[ab[i][0]].add(ab[i][1])
        dic[ab[i][1]].add(ab[i][0])
    leng = [-1] * n
    qu = deque()
    qu.append(1)
    leng[0] = 0
    while len(qu) > 0:
        z = qu.popleft()
        for j in dic[z]:
            if leng[j - 1] == -1:
                qu.append(j)
                leng[j - 1] = leng[z - 1] + 1
    for i in range(q):
        if (leng[cd[i][0] - 1] + leng[cd[i][1] - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")
    return


input = sys.stdin.readline
#n=int(input())
#s=input()[:-1]
#t=input()[:-1]
#s2=input()[:-1]
#s3=input()[:-1]
#s=input()[:-1]
#a=list(map(int,input().split()))
#q=int(input())
#b=list(map(int,input().split()))
#c=list(map(int,input().split()))
n, q = map(int, input().split())
#c=list(map(int,input().split()))
#b=list(map(int,input().split()))
#a=set(map(int,input().split()))
#b=set(map(int,input().split()))
ab = [None for _ in range(n - 1)]
#ddn=gen_d(n,p)
#a=list()
#c=list()
for i in range(n - 1):
    #  k=int(input())
    ab[i] = list(map(int, input().split()))
cd = [None for _ in range(q)]
#ddn=gen_d(n,p)
#a=list()
#c=list()
for i in range(q):
    #  k=int(input())
    cd[i] = list(map(int, input().split()))
#  main(k,a,n)
#  s[i]=input()[:-1]
#  u,d=map(int,input().split())
#  s.append(ddn[u][d])
#print("\n".join(list(map(str, s))))
#  a[i]=input()[:-1]
#p=[None for _ in range(50)]
#for _ in range(31):
#  p[i]=list(map(int,input().split()))
#  s[i]=input()[:-1]
#  main(input()[:-1])
#q=int(input())
#x=list(map(int,input().split()))
#n=int(input())
#f=list(map(int,input().split()))
#z=main(n,m,q,wv,x)
#b=np.array(list(map(int,input().split()))).astype(int)
#for i in range(q):
#p=list(map(int,input().spln,xyit()))
#	l,r=map(int,input().split())
#	print(z[l-1][r-1])
main(n, q, ab, cd)
