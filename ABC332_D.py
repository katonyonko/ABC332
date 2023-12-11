import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
1 3 2 5 4
11 13 12 15 14
6 8 7 10 9
16 18 17 20 19
2 2
1 1
1 1
1 1
1 1000000000
3 3
8 1 6
3 5 7
4 9 2
8 1 6
3 5 7
4 9 2
5 5
710511029 136397527 763027379 644706927 447672230
979861204 57882493 442931589 951053644 152300688
43971370 126515475 962139996 541282303 834022578
312523039 506696497 664922712 414720753 304621362
325269832 191410838 286751784 732741849 806602693
806602693 732741849 286751784 191410838 325269832
304621362 414720753 664922712 506696497 312523039
834022578 541282303 962139996 126515475 43971370
152300688 951053644 442931589 57882493 979861204
447672230 644706927 763027379 136397527 710511029
"""

def solve(test):
  H,W=map(int, input().split())
  A=[list(map(int, input().split())) for _ in range(H)]
  B=[list(map(int, input().split())) for _ in range(H)]
  ans=10000
  for p1 in permutations(range(H)):
    for p2 in permutations(range(W)):
      flg=0
      for i in range(H):
        if flg==1: break
        for j in range(W):
          if flg==1: break
          if A[p1[i]][p2[j]]!=B[i][j]:
            # print(p1,p2,i,j)
            flg=1
      if flg==1: continue
      tmp=0
      for i in range(H):
        for j in range(i+1,H):
          if p1[i]>p1[j]:
            tmp+=1
      for i in range(W):
        for j in range(i+1,W):
          if p2[i]>p2[j]:
            tmp+=1
      ans=min(ans, tmp)
  if test==0:
    if ans==10000:
      print(-1)
    else:
      print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)