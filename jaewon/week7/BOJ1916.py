import sys
import heapq

# 최소비용 구하기 - 특정 구간 최단거리
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())  # a->b 비용 c
    graph[a].append((b, c))

# 출발점, 도착점
start, end = map(int, input().split())

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 인접 노드 확인
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

dijkstra(start)
print(distance[end])

