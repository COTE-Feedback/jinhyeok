def insertion_sort_kth(A, N, K):
    cnt = 0

    for i in range(1, N):
        loc = i - 1
        newItem = A[i]

        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
            cnt += 1

        if loc + 1 != i:
            A[loc + 1] = newItem
            cnt += 1

        if cnt >= K:
            return A[i - 1]

    return -1

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 삽입 정렬 수행 및 결과 출력
result = insertion_sort_kth(A, N, K)
print(result)

