# 병합정렬 사용코드 
import sys

def bubble_sort(arr):
    global cnt
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                cnt += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap


n = int(input())
l1 = list(map(int, sys.stdin.readline().split()))
cnt = 0
# print(l1)
bubble_sort(l1)
print(l1)
print(cnt)

