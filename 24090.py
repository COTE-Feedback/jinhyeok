def quick_sort(A, p, r, K):
    if p < r:
        q = partition(A, p, r)
        if q == K - 1:
            print(A[q], A[q + 1])
            return
        elif q > K - 1:
            quick_sort(A, p, q - 1, K)
        else:
            quick_sort(A, q + 1, r, K - q - 1)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 초기 호출
if K <= N - 1:
    quick_sort(A, 0, N - 1, K)
else:
    print(-1)
