import sys

N = sys.stdin.readline()
A = set(sys.stdin.readline().strip().split(" "))
M = sys.stdin.readline()
arr = sys.stdin.readline().strip().split(" ")

for num in arr:
    print(1) if num in A else print(0)