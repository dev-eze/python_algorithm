'''
최단 경로 문제
• 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미합니다.
• 다양한 문제 상황
    • 한 지점에서 다른 한 지점까지의 최단 경로
    • 한 지점에서 다른 모든 지점까지의 최단 경로
    • 모든 지점에서 다른 모든 지점까지의 최단 경로
• 각 지점은 그래프에서 노드로 표현
• 지점 간 연결된 도로는 그래프에서 간선으로 표현

'''

'''
다익스트라 최단 경로 알고리즘 개요
• 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.
• 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작합니다. -> 현실세계 길 찾기 문제
    • 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않습니다.
• 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됩니다.
    • 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.
'''

'''
다익스트라 최단 경로 알고리즘
• 알고리즘의 동작 과정은 다음과 같습니다.
1. 출발 노드를 설정합니다.
2. 최단 거리 테이블을 초기화합니다. (자기자신은 0, 나머지는 무한대)
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다. -> 그리디
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다. -> 초기화 이후 3,4번 박복
5. 위 과정에서 3번과 4번을 반복합니다.

• 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있습니다.
• 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이 경로가 제일 짧은 경로야'라고 갱신합니다.

• 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.
• 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않습니다.
• 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있습니다.
• 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됩니다.
• 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 합니다.
'''
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

try:
    n, m = map(int, input().split())  # 노드의 개수, 간선의 개수
except KeyboardInterrupt:
    print("프로그램이 사용자에 의해 중단되었습니다.")

start = int(input()) # 시작 노드 번호 입력
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문여부 리스트
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int,  input.split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_minimum_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def daikstra(start):
    # 사적 노드에 대해 초기화
    distance[start] = 0
    # 시작 노드 방문처리
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

# 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_minimum_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드들 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 실행
daikstra(start)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


'''
다익스트라 알고리즘: 간단한 구현 방법 성능 분석
• 총 0(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 합니다.
• 따라서 전체 시간 복잡도는 O(V2)입니다.
• 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결할 수 있습니다.
• 하지만 노드의 개수가 10,000개를 넘어가는 문제라면 ?

파이썬 1초 = 2000만번

'''

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
