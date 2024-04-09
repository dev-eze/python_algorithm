# 연결 요소(Connected Component)를 찾는 방법은 그래프 이론에서 주어진 그래프 내에서 각각의 서로 연결된 부분을 식별하는 작업
# DFS(Depth-First Search, 깊이 우선 탐색)나 BFS(Breadth-First Search, 너비 우선 탐색) 알고리즘을 사용하는 것이 일반적
# 음료수 얼려 먹기 : connected component 찾기

from collections import deque

def dfs(x, y):  # 상하좌우에 00이면 방문처리후 카운팅
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문 처리
        # 상하좌우 체크
        # 상 (x-1, y)
        # 하 (x+1, y)
        # 좌 (x, y-1)
        # 우 (x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
n, m = 3, 3
graph = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

count = 0
for i in range(n):
    for j in range(m):
        if (dfs(i, j) == True):
            count += 1
print(count)



