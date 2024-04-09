# 2차원 공간, 행렬
# for i in range(5):
#     for j in range(5):
#         print("(", i, ",", j, ")", end=" ")
#         print()

# 상하좌우
# nxn, 가장 왼쪽은 (1,1), 시작 좌표 1,1
# 입력 5, r r r u d d
# 출력 3, 4
def getCurrentLocation():
    n = 5
    x, y = 1, 1
    directions = ["L", "R", "U", "D"]
    plans = ["R", "R", "R", "U", "D", "D"]
    dx = [0, 0 , -1, 1]
    dy = [-1, 1, 0, 0]
    for plan in plans:
        for i in range(len((directions))):
            if plan == directions[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        else:
            x, y = nx, ny
    return(x, y)

print(getCurrentLocation())

# 시각 문제
'''
00시 00분 00초부터 n시 59분 59초까지 3이 하나라도 포함되는 모든 경우의 수
입력: 5
출력: 11475
제한: 0 <= n <= 23
'''
def getThreeCount():
    n = 5
    count = 0
    # 시 분 초
    minute_second = 60
    for i in range(n+1 ):
        for j in range(minute_second):
            for k in range(minute_second):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count
print(getThreeCount())
