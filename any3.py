n = int(input())

def get_count(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        count += 1
    return count

print(get_count(n))


# 두 정수사이에서 맥스 우박수 길이를 구하는건, getcount를 a, b사이의 모든 수에 대해 실행하고, 가장 큰 값을 출력하면 된다.
a, b = map(int, input().split())
max_count = 0
for i in range(a, b+1):
    count = get_count(i)
    if count > max_count:
        max_count = count
print(max_count)