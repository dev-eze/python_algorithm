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