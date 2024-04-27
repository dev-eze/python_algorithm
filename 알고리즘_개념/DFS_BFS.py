graph = [
    [], # 0번 노드는 없으므로 비워둠
    [2, 3, 8], # 1번 근접 노드 2, 3, 8
    [1, 7], # 2번 근접노드 1, 7
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# DFS 예제 stack
# 인접노드에서 번호가 낮은 인접노드부터 방문
# 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5
# 방문한 노드를 체크하기 위한 리스트
visited_dfs = [False] * 9 # 인덱스 0은 사용하지 않기 때문에 9개로 설정
def dfs(graph, index, visited):
    visited[index] = True
    print(index, end=' -> ')
    for i in graph[index]:
       if not visited[i]: # 방문하지 않은 노드라면
           dfs(graph, i, visited)
print(dfs(graph, 1, visited_dfs)) # 1번 노드부터 시작


# BFS 예제 queue
# 인접노드중 방문하지 않은 모든 노드를 모두 큐에 삽입하고 방문처리
# 1-> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6
# 가능성이 같은 경우에서 최단 거리 구하는 경우에 사용
from collections import deque
visited_bfs = [False] * 9
def bfs(graph, index, visited_bfs):
    visited_bfs[index] = True
    que = deque([index])
    while que:
        index = que.popleft()
        print(index, end=' -> ')
        for i in graph[index]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                que.append(i)
print(bfs(graph, 1, visited_bfs))