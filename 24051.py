def insertion_sort(A, N, K):
    for i in range(1, N):
        loc = i - 1
        newItem = A[i]

        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1

        if loc + 1 != i:
            A[loc + 1] = newItem

        if i == K:
            return A[K - 1]

    return -1

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 삽입 정렬 수행 및 결과 출력
result = insertion_sort(A, N, K)
print(result)
