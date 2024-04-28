def maxAreaOfIsland_dfs(grid):
    m, n = len(grid), len(grid[0])

    def dfs(x, y):
        # 현재 위치가 그리드 범위를 벗어나거나, 바다(0)일 경우 0을 반환
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 0
        # 현재 땅을 방문 처리 (재방문 방지를 위해 0으로 설정)
        grid[x][y] = 0
        # 현재 위치에서 상하좌우를 탐색하여 크기 계산
        area = 1  # 현재 위치도 섬의 일부이므로 1부터 시작
        area += dfs(x + 1, y)
        area += dfs(x - 1, y)
        area += dfs(x, y + 1)
        area += dfs(x, y - 1)
        return area

    max_area = 0
    # 모든 셀에 대해 DFS 실행
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                # 현재 위치에서 시작하는 섬의 크기를 계산하고, 최대값을 갱신
                max_area = max(max_area, dfs(i, j))

    return max_area

# 예시 입력 및 실행
grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1]]
print(maxAreaOfIsland(grid))  # 출력: 4

from collections import deque


def maxAreaOfIsland_bfs(grid):
    m, n = len(grid), len(grid[0])

    def bfs(x, y):
        queue = deque([(x, y)])
        grid[x][y] = 0  # 방문한 위치는 0으로 설정하여 중복 방문 방지
        area = 1

        while queue:
            cur_x, cur_y = queue.popleft()
            # 상하좌우 이동을 위한 방향 벡터
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                # 새 위치가 그리드 내에 있고, 땅('1')일 경우
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0  # 방문 처리
                    queue.append((nx, ny))
                    area += 1
        return area

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, bfs(i, j))

    return max_area


# 예시 입력 및 실행
grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1]]
print(maxAreaOfIsland(grid))  # 출력: 4

from collections import deque


def numIslands(grid):
    m, n = len(grid), len(grid[0])

    def bfs(x, y):
        queue = deque([(x, y)])
        grid[x][y] = '0'  # 방문한 위치는 '0'으로 설정하여 중복 방문 방지

        while queue:
            cur_x, cur_y = queue.popleft()
            # 상하좌우 이동을 위한 방향 벡터
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                # 새 위치가 그리드 내에 있고, 땅('1')일 경우
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'  # 방문 처리
                    queue.append((nx, ny))

    island_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                bfs(i, j)
                island_count += 1  # 새 섬을 발견할 때마다 카운트 증가

    return island_count


# 예시 입력 및 실행
grid = [
    ["1", "1", "0", "0"],
    ["1", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "0", "0", "1"]
]
print(numIslands(grid))  # 출력: 3



