n = int(input())
# 좌표 = [input().join(" ") for i in range(n)]
좌표 = [list(map(int, input().split())) for i in range(n)]

def 좌표정렬(좌표):
    정렬된좌표 = sorted(좌표, key=lambda x: (x[0], x[1]))

    for x, y in 정렬된좌표:
        print(f"{x} {y}")


좌표정렬(좌표)