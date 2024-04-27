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

# 왕실의 나이트
'''
8x8 좌표 평면, 나이트가 이동할 수 있는 경우의 수
- 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
- 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동
- 행 1~8, 열 a~h
입력: a1
출력: 2
입력: c2
출력: 6
'''
def getKnightCount():
    # 8가지 이동 가능한 방향에대한 벡터 정의
    directions = [(-2, -1),  (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    char_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    input_data = "c2" # 행 1 열 a
    x = int(input_data[1])
    y = int(char_to_num[input_data[0]])
    print(x, y)
    result = 0

    for i in directions:
        nx = x + i[0]
        ny = y + i[1]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            print("범위 벗어남")
            continue
        elif nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8: # 체스판 범주에 있다면 카운팅
            result += 1
    return result
print(getKnightCount())


# 문자열 재정렬
'''
    알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐
    알파벳 오름차순으로 정렬 + 모든 숫자를 합한 값을 이어서 출력
    
    입력: K1KA5CB7
    출력: ABCKK13
    
    입력: AJKDLSI412K4JSJ9D
    출력: ADDIJJJKKLSS20
'''

def getReorderString():
    input_data = "K1KA5CB7"
    result = []
    number_sum = 0
    dataList = list(input_data)

    for i in dataList:
       if i.isalpha():
            result.append(i)
       else:
           number_sum += int(i)

    result.sort()

    if number_sum != 0:
        result.append(str(number_sum))
    return "".join(result)
print(getReorderString())
