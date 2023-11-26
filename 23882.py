import sys

n, exchange = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
swap = 0


def selection(arr):
    global swap
    result = []

    for i in range(n - 1, 0, -1):
        max, index = arr[0], 0

        for j in range(0, i + 1):
            if arr[j] > max:
                max, index = arr[j], j

        if i != index:
            arr[i], arr[index] = arr[index], arr[i]
            swap += 1

            if swap == exchange:
                result.append(arr[index])
                result.append(arr[i])
                return result

    result.append(-1)
    return result


print(*selection(arr))

# *(Asterisk): Unpacking 역할 ->쉽게 말해서 괄호 안에 있던 데이터들을 풀어 각각으로 만들어 줌
