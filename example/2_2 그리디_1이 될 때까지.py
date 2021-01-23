def make1(N, K):
    count = 0
    while N != 1:
        if N % K == 0:
            N = N / K
            count += 1
        else:
            N = N - 1
            count += 1
    return count


#################################################

result = 0
N = 25
K = 3
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K
    result += (N - target)
    N = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break

    # K로 나누기
    result += 1
    N = N // K

# 마지막으로 남은 수에 대하여 1이 남을때 까지 빼기
result += (N - 1)
print(result)

# 위의 두 방법은 시간 복잡도 측면에서 차이가 있다.
# 아래 코드는 시간 복잡도가 log시간 복잡도 이므로 값이 커져도 빠르게 실행할 수 있다.
