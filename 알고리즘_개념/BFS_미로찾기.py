from collections import deque
# 미로 탈출 : 최단거리 찾기
# BFS로 구현
# 0은 괴물이 있는 부분, 1은 괴물이 없는 부분
# 1, 1에서 시작하여 n, m으로 이동하는 최소 칸의 개수 구하기 *시작칸과 마지막칸 포함
'''
입력 예시
5 6 -> 10
101010
111111
000001
111111
111111
'''
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
n, m = 3, 3
graph = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]
def bfs(x, y):
    # 상 하 좌 우
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(len(directions)):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 범위 벗어난 경우
                continue # 계속 다음으로 진행
            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue # 계속 다음으로 진행

            # 괴물이 없는 경우에만 거리 이동 + 1
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))

    result = graph[n-1][m-1] # 인덱스를 0부터 시작해서 -1
    return result
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(bfs(0, 0))
