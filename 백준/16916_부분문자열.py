'''
부분 문자열
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	16421	5139	3828	36.607%
문제
문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.

예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.

문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

입력
첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다. 두 문자열은 빈 문자열이 아니며, 길이는 100만을 넘지 않는다. 또, 알파벳 소문자로만 이루어져 있다.

출력
P가 S의 부분 문자열이면 1, 아니면 0을 출력한다.
'''
s = 'baekjoon'
p = 'aek'
import sys
# s = sys.stdin.readline()
# p = sys.stdin.readline()
#s, p = (input().rstrip() for _ in range(2))
def solution(s, p):
    #return 1 if p in s else 0
    return 1 if s.__contains__(p) else 0

print(solution(s, p))
