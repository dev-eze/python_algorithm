import heapq
import sys

input = sys.stdin.readline()
# 노드 개수, 간선 개수
n, m = map(int, input.split())
start = int(input())

graph = [[] for i in range(n+1)] # n개만큼 생성, 0은 비워둠.
INF = int(1e9)
distance = [INF] * n+1

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b,c)
    # a노드에서 b노드로 가는 비용이 c라는 의미
    # graph[a] = b,c
    ##  -> graph[0] 인접노드 ,  graph[1] 인접노드와의 거리

def getminimum(start_node):
    q = []
    #시작노드로 가기 위한 최단 거리를 0으로 설정해서 q에 삽입
    heapq.heappush(q, (0, start_node)) # 최단거리0, start
    distance[start_node] = 0

    while q: # q가 비어있지 않다면
        # 가장 최단 거리 노드에 대한 정보 꺼내기
        guri, now_node = heapq.heappop(q)
        # 현재 노드가 처리된적이 있는 노드인경우 무시
        if distance[now_node] < guri: # guri 더 크다면 이미 처리된것으로 간주할 수 있음
            continue
        # 현재 노드와 인접노드 확인하기
        for i in graph[now_node]: # i[1] 거리, i[0] 인접 노드
            cost = guri + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


getminimum(start_node)

for i in range(1, n+1):
    if distance[i] == INF:
        print("inf")
    else
        print(distance[i])