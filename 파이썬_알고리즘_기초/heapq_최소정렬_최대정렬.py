import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힘에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



def heapsort_desc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힘에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(heapsort_desc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

import heapq


#최단거리 heapq
def dijkstra(graph, start):
    # 무한대를 나타내는 값 설정
    INF = float('inf')
    # 거리를 저장할 딕셔너리, 시작점의 거리는 0으로 초기화
    distances = {node: INF for node in graph}
    distances[start] = 0
    # 모든 노드를 방문할 때까지
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # 우선순위 큐에서 거리가 가장 짧은 노드 선택
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재 노드의 거리가 저장된 거리보다 크면 무시
        if distances[current_node] < current_distance:
            continue

        # 현재 노드와 인접한 노드들의 거리 갱신
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            # 만약 새로 계산한 거리가 기존 거리보다 작으면 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))

    return distances


# 그래프는 딕셔너리를 이용하여 인접 리스트 형태로 표현
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)