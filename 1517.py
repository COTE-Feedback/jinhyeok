import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
length = len(arr)

swap_cnt = 0

for i in range(length):
  for j in range(0,length - i - 1):
    if arr[j] > arr[j+1]:
      swap_cnt += 1
      arr[j], arr[j+1] = arr[j+1], arr[j]

print(swap_cnt)

# 시간초과