from collections import deque
n = int(input())  # 마을의 크기
graph = [list(map(int, input().split())) for _ in range(n)]
def bfs(graph, visited, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # matrix 범위 내에 있고, 방문하지 않은 집이 있는 경우
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
def min_generators(graph):
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 집을 발견하면 발전기 수 증가 및 BFS 수행
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(graph, visited, (i, j))
                result += 1
    return result

print(min_generators(graph))

