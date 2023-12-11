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
5 3
3 5 3 6 3
"""

def solve(test):
  N,D=map(int, input().split())
  W=list(map(int, input().split()))
  dp=[-1]*(2**N*D)
  tmp=[0]*(1<<N)
  for i in range(1<<N):
    for j in range(N):
      if (i>>j)&1:
        tmp[i]+=W[j]
  def idx(s,d):
    return s*D+d
  for i in range(D):
    for j in range(1<<N):
      if i==0: dp[idx(j,0)]=tmp[j]**2
      else:
        subs=(j-1)&j
        while subs!=0:
          if dp[idx(j-subs,i-1)]>=0:
            if dp[idx(j,i)]<0: dp[idx(j,i)]=dp[idx(subs,0)]+dp[idx(j-subs,i-1)]
            else: dp[idx(j,i)]=min(dp[idx(j,i)],dp[idx(subs,0)]+dp[idx(j-subs,i-1)])
          subs=(subs-1)&j
  ans=(min([dp[idx((1<<N)-1,d)] for d in range(D) if dp[idx((1<<N)-1,d)]>=0])*D-sum(W)**2)/(D**2)
  if test==0:
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