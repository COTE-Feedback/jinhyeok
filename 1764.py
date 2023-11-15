import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = dict()
answer = []
for i in range(n):
    x = input()
    if x not in arr1:
        arr1[x] = i

for i in range(m):
    y = input()
    if y in arr1:
        answer.append(y)
# x,y를 모두 만족하는 사람을 구해야됨 - arr1에 있는 이름과 겹치는 y만 구해서 answer에 넣음
answer.sort()
print(len(answer))
print(''.join(answer), end = '')