n = 25
k = 3 # 6

def solution(n, k):
    count = 0

    while True:
        multiple_target = (n // k) * k
        count += (n - multiple_target) # 1로 뺴는 횟수
        n = multiple_target

        if n < k :
            break

        count += 1
        n //= k
    # n이 1보다 큰 경우
    count += (n - 1)
    return count

print(solution(n, k))

def solution2(n, k):
    count = 0
    while True:
        if n < k: # 무한반복문을 빠져나갈 조건을 반드시 먼저 생각하자!
            break

        elif n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1

    return count + (n-1) if n != 1 else n

print(solution2(n, k))