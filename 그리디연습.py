# 그리디 - 최소 거스름돈 문제
coins = [500, 100, 50, 10]

def min_coin_count(money, coins):
    count = 0
    for coin in coins:
        count += money // coin
        money %= coin
    return count

print(min_coin_count(4720, coins)) # 31

# 그리디 - n이 1일 될 떄 까지의 최소 과정 횟수 구하기
'''
n이 1이 될 떄 까지 아래 과정 반복
1. n에서 1을 뺀다
2. n이 k로 나누어 떨어질때에만 n을 k로 나눈다
'''
n = 25
k = 3
def get_min_count(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        count += 1
    return count

print(get_min_count(n, k))

def getminCount(n, k):
    result = 0
    while True:
        max = n//k
        target = k * max
        result += (n - target)

        n = target
        if n < k: # 더이상 나눌 수 없는경우
            break

        result +=1
        n //= k

    result += (n-1)
    return result
print(getminCount(n, k))

# 그리디 - 곱하기 혹은 더하기
def getMax(s):
    # 1<= s <=20
    data = list(map(int, s))
    result = data[0]
    for i in range(len(data)):
        if i <= 1 or result <= 1:
            result += data[i]
        else:
            result *= data[i]

    return result
print(getMax("0123"))

# 모험가 길드
# 입력:n = 5, 23122 출력:2
def getmaxgroup():
    n = 5
    group = [2, 3, 1, 2, 2]
    group.sort() # 1 2 2 2 3

    max_group = 0
    member = 0
    for i in range(n):
        member += 1
        if member >= group[i]:
            max_group += 1
            member = 0 # 그룹 달성후 멤버 수 초기화
    return max_group
print(getmaxgroup())


