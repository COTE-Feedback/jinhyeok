#1158 , 10866번
def josephus(N, K):

    lst = [i for i in range(1, N+1)]
    # 제거된 사람들을 담을 결과 리스트
    result = []
    # 리스트에서 노드를 순서대로 탐색하여 제거
    i = 0
    while lst: # 1st가 비어있을 때까지 반복
        i = (i+K-1) % len(lst)  #첫번째값의 인덱스가 0 -> K-1 사용

        result.append(lst.pop(i))
    return result


N, K = map(int,input().split())
result = josephus(N,K)
print(result)