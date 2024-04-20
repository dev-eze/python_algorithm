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