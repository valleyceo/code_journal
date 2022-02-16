import sys

T = int(input())

for t in range(1, T + 1):
  N, M = input().split()
  Arr = input().split()
  total = sum(map(lambda x : int(x), Arr))
  print("Case #{}: {}".format(t, total % int(M)))
