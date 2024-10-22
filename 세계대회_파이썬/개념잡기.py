import math
## 우선순위 큐 (단순 순회는 우선순위를 보장하지 않는다.)
# from queue import PriorityQueue
#
# q = PriorityQueue()
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(5)
#
# # print(len(q.queue))
# # print(q.get())
# print(q.queue)
# # print(len(q.queue))
# print(q.queue[0])
# print(q.queue)
#
# while q.queue:
#     print(q.get(), end=' ', sep=' ')
#
# print('\n')
#
# pq = PriorityQueue()
# pq.put([-10, 10])
# pq.put([-20, 20])
# pq.put([-5, 5])
# pq.put([-30, 30])
# # print(len(q.queue))
# # print(q.get())
#
# # print(len(q.queue))
# print(pq.queue[0])
# print(pq.queue)
#
# while pq.queue:
#     print(pq.get()[1], end=' ')


## 셋 집합
# set_a = {1,2,3,4,5}
# set_b = {2,4,6,8,10}
# print (set_a | set_b)
# print (set_a & set_b)
# print (set_a - set_b)

# ## 약수 구하기
# def 약수구하기(n):
#     divisors = set()
#     if n <= 1:
#         return divisors.add(1)
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors.add(i)
#     return divisors
#
#
# print(약수구하기(18))
#
# from math import sqrt
# def 더빠른약수구하기(n):
#     divisors2 = set()
#     if n <= 1:
#         return divisors2.add(1)
#     for i in range(1, int(sqrt(n))+1):
#         if n % i == 0:
#             divisors2.add(i)
#             divisors2.add(n // i)
#             print(n//i, n, i)
#     return divisors2
#
#
# print(더빠른약수구하기(18))

# # 소수 : 1과 자기 자신만을 약수로 가지는 수
# from math import sqrt
#
# def 더빠른약수구하기(n):
#     divisors2 = set()
#     if n <= 1:
#         return divisors2.add(1)
#     for i in range(1, int(sqrt(n))+1):
#         if n % i == 0:
#             divisors2.add(i)
#             divisors2.add(n // i)
#
#     return divisors2
#
# def 소수판별(n):
#     if (len(더빠른약수구하기(n)) == 2):
#         return True
#     return False
#
# print(소수판별(2))
# print(소수판별(7))
# print(소수판별(18))
# print(소수판별(9))

## 최소 공약수 gcd (greate common divisor) : 두수의 공약수중 가장 큰 수
## 최소 공배수 lcm (least common multiple) : 두수의 공배수중 가장 작은 수

# from math import gcd, sqrt
# print(gcd(12, 6))
#
# def 더빠른약수구하기(n):
#     divisors = set()
#     if n <= 1:
#         return divisors.add(1)
#     for i in range(1, int(sqrt(n))+1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#
#     return divisors
#
# def 최대공약수구하기(a, b):
#     a = 더빠른약수구하기(a)
#     b = 더빠른약수구하기(b)
#     return max(a & b)
#
# print(최대공약수구하기(12, 6))
#
# def 최소공배수구하기(a, b):
#     # 두수의 곱은 = 최대공약수 * 최소공배수와 같다.
#     return a * b // 최대공약수구하기(a, b)
#
# print(최소공배수구하기(3, 12))


# ## 소인수 분해 : 소수들의 곱으로만 나타내는것
# def 소인수분헤(n):
#     primes = []
#     for i in range(2, n+1):
#         while n % i == 0:
#             primes.append(i)
#             n //= i # i로 나눈 몫 다시 n에 저장
#     return primes
#
# print(소인수분헤(60))
# print(소인수분헤(37))

# ## 에라토스테네스의 체 알고리즘 : 원리는 두 수의 최대공약수는 두 수 중 작은 수로 큰 수를 나눈 나머지와 작은 수의 최대공약수와 같다. 즉 b가 0일때 a의 값이 최대 공약수
# 에라토스테네스의체 = 120
#
# def 에라토스테네스체(n):
#     is_primes = [True] * (n + 1)
#     is_primes[0] = False
#     is_primes[1] = False
#     for i in range(2, int(n**0.5)):
#         if is_primes[i]:
#             for j in range(i*i, n+1, i):
#                 is_primes[j] = False
#     return list(filter(lambda x: is_primes[x], range(2, n+1)))
#
#     # return [x for x in range(2, n+1) if is_primes[x]]
#     # return list(filter(lambda x: is_primes[x], range(2, n + 1)))
#
# print(에라토스테네스체(120))

# ## 유클리드호제 최대공약수
# def 유클리드호제_최대공약수구하기(a, b):
#     if b == 0:
#         return a
#     return 유클리드호제_최대공약수구하기(b, a % b)
#
# print(유클리드호제_최대공약수구하기(12, 8))


# 수식 정리

# import sys
# input = sys.stdin.readline().rstrip()
# print(input)


# 피보나치 수열
# F(n)=F(n−1)+F(n−2) (n ≥ 2)

def 피보나치재귀(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 피보나치재귀(n-1) + 피보나치재귀(n-2)

print(피보나치재귀(10))

def 피보나치동적(n):
    list = [0, 1]
    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])
    return list[n]

print(피보나치동적(10))

def 피보나치메모이제이션(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = 피보나치메모이제이션(n-1, memo) + 피보나치메모이제이션(n-2, memo)
        return memo[n]
print(피보나치메모이제이션(10))
