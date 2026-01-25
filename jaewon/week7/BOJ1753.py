import sys
import heapq

# 최단경로 - 기본 다익스트라 알고리즘
input = sys.stdin.readline
INF = int(1e9)

# 정점의 개수 V, 간선의 개수 E
v, e = map(int, input().split())
# 시작 정점 번호
start = int(input())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())  # a->b로 가는 가중치 c
    graph[a].append((b, c))

# 최단 거리 테이블 초기화
distance = [INF] * (v + 1)

def dijkstra(start):
    # 우선순위 큐 사용 (거리, 노드)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접 노드 확인
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            
            # 현재 노드를 거쳐서 가는 것이 더 짧은 경로라면
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

dijkstra(start)

# 결과 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

