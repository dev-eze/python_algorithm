'''
최단 거리 문제를 해결할 때 Python 딕셔너리를 사용하는 한 가지 일반적인 방법은 그래프 데이터 구조에서의 다익스트라 알고리즘을 구현하는 것입니다.
딕셔너리는 노드 간의 연결과 비용(거리, 가중치)을 표현하기에 매우 적합합니다.

다음 예제는 간단한 가중치 그래프를 딕셔너리로 표현하고, 시작 노드에서 다른 모든 노드까지의 최단 거리를 계산하는 다익스트라 알고리즘을 구현한 것입니다:

이 코드는 다음을 수행합니다:

그래프 초기화: 그래프는 각 노드에 대한 인접 노드와 해당 가중치를 포함하는 딕셔너리로 표현됩니다.
거리 딕셔너리: 모든 노드에 대한 거리를 무한대로 초기화하고, 시작 노드의 거리는 0으로 설정합니다.
우선순위 큐 사용: 현재 노드에서 가장 짧은 거리를 가진 노드를 효율적으로 선택하기 위해 힙(우선순위 큐)을 사용합니다.
거리 업데이트: 현재 노드와 인접한 노드들의 거리를 계산하고, 필요한 경우 최단 거리 정보를 업데이트하며, 업데이트된 거리 정보를 큐에 다시 삽입합니다.
이 알고리즘은 그래프의 모든 노드와 경로에 대해 최단 거리를 효율적으로 찾을 수 있으며, 딕셔너리를 사용하여 각 노드의 인접 노드와 가중치 정보를 쉽게 관리할 수 있습니다.

'''

import heapq


def dijkstra(graph, start):
    # 거리 정보를 저장할 딕셔너리, 무한대로 초기화
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # 시작 노드의 거리는 0
    # 우선순위 큐 초기화
    priority_queue = [(0, start)]

    while priority_queue:
        # 가장 짧은 거리의 노드 선택
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드는 건너뛰기
        if current_distance > distances[current_node]:
            continue

        # 인접 노드 거리 업데이트
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 거리를 찾았다면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 그래프는 딕셔너리로 표현
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 'A'에서 시작
start_node = 'A'
distances = dijkstra(graph, start_node)
print("Distances from node", start_node, ":", distances)
