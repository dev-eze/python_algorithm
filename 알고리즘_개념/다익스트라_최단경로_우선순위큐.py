'''
우선순위 큐(Priority Queue)
• 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
• 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있습니다.
• Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원합니다.
• 우선순위 큐를 이용하면 다익스트라 최단 경로 알고리즘을 더욱 빠르게 구현할 수 있습니다.
자료구조
추출되는 데이터
스택(Stack)
가장 나중에 삽입된 데이터
큐(Queue)
가장 먼저 삽입된 데이터
우선순위 큐(Priority Queue)
가장 우선순위가 높은 데이터


힙(Heap)
• 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나입니다.
• 최소 힙(Min Heap) -> 낮은값 과 최대 힙(Max Heap) ->높은값부터 이 있습니다.
• 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됩니다.

우선순위 큐 구현 방식        삽입 시간             삭제 시간
리스트                     0(1)                O(N)
힙(Heap)                 0(logN)             0(logN)

'''

import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort_asc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        #  heapq.heappush() 이 함수를 호출하면, 주어진 원소가 힙 자료구조에 추가되며, 힙의 속성(최소 힙의 경우 부모 노드가 자식 노드보다 항상 작거나 같다는 속성)이 유지되도록 원소가 적절한 위치에 삽입
    # 힘에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        # heapq.heappop은 Python의 heapq 모듈에 있는 함수로, 힙 자료구조에서 가장 작은 원소를 제거하고 그 원소를 반환.
    return result

print(heapsort_asc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
이 코드는 Python의 heapq 모듈을 사용하여 주어진 리스트를 오름차순으로 정렬하는 힙 정렬 알고리즘을 구현.
  
h = []와 result = []를 통해 빈 리스트 두 개를 생성. 
h는 힙 자료구조를 위한 것이고, result는 정렬된 결과를 저장하기 위함.
for value in iterable: 반복문을 통해 입력받은 리스트의 각 원소를 순회. 
각 원소를 heapq.heappush(h, value)를 사용하여 힙 h에 삽입. 
이 때, heapq 모듈은 자동으로 최소 힙 구조를 유지.  
for i in range(len(h)): 반복문을 통해 힙 h에 삽입된 모든 원소를 차례대로 꺼냄. 
heapq.heappop(h)를 사용하여 힙에서 가장 작은 원소를 꺼내 result 리스트에 추가.  
모든 원소를 꺼내서 result에 저장한 후, result를 반환. 이 result는 입력 리스트의 오름차순 정렬된 상태로 출력됨.
'''

# 기본은 오름차순 정렬이나 내림차순 정렬시
# heapq.heappush(h, -value)와 -heapq.heappop(h)를 사용하면 됨.
def heapsort_desc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
        #  heapq.heappush() 이 함수를 호출하면, 주어진 원소가 힙 자료구조에 추가되며, 힙의 속성(최소 힙의 경우 부모 노드가 자식 노드보다 항상 작거나 같다는 속성)이 유지되도록 원소가 적절한 위치에 삽입
    # 힘에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
        # heapq.heappop은 Python의 heapq 모듈에 있는 함수로, 힙 자료구조에서 가장 작은 원소를 제거하고 그 원소를 반환.
    return result

print(heapsort_desc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
다익스트라 알고리즘: 개선된 구현 방법
• 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용합니다.
• 다익스트라 알고리즘이 동작하는 기본 원리는 동일합니다.
• 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다릅니다.
• 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용합니다.

다익스트라 알고리즘: 개선된 구현 방법 성능 분석
• 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)입니다.
• 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않습니다.
• 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있습니다.
• 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사합니다.
• 시간 복잡도를 O(ElogE)로 판단할 수 있습니다.
• 중복 간선을 포함하지 않는 경우에 이를 0(ElogV)로 정리할 수 있습니다.
• 0(ElogE) → 0(ElogV^2) → 0(2ElogV) → 0(ElogV)
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 18억을 설정 # 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]* (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra_heap(start):
    q = []
    #시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now= heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
# 다익스트라 알고리즘을 수행
dijkstra_heap(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        result = distance[i]
        print(result)