# 팩토리얼 구현
# 반복문
def factorial(n):
    result = 1 # 0!, 1! = 1
    for i in range(1, n+1):
        result *= i
    return result
# 재귀함수
def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
       return n * factorial_recursive(n-1)

print(factorial(5))
print(factorial_recursive(5))

# 유클리드 호제법
# 192, 162 -> 192 % 162 = 30 -> 162 % 30 = 12 -> 30 % 12 = 6 -> 12 % 6 = 0
def gcd_recursive(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd_recursive(b, r)
print(gcd_recursive(192, 162))