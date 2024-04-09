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