# 백준 4779번 문제 칸토어 집합
import sys


# def solution(n):
#     if n == 1:
#         return "-"
#     else:
#         print('n//3:'+n//3)
#         left = solution(n//3)
#         empty_center = " " * n//3
#         return left + empty_center + left
#
# while True:
#     try:
#         # n = int(input())
#         n = int(sys.stdin.readline().rstrip())
#
#         result = solution(3^n)
#     except:
#         break
#
#
#

def solution(n):
    if n == 1:
        return "-"
    else:
        left = solution(n // 3)
        center = " " * (n // 3)
    return left + center + left

# while True:
#     try:
#         N = int(input())
#         result = solution(3 ** N)
#         print(result)
#     except:
#         break


def solution2(n):
    if n == 0:
        return "-"
    else:
        left = solution2(n-1)
        center = " " * (3**(n-1))
    return left + center + left

while True:
    try:
        n = int(input())
        result = solution2(n)
        print(result)
    except:
        break
