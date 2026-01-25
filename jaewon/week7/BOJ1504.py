import sys
import heapq

# 특정한 최단 경로 - 특정 정점을 반드시 거치는 최단경로
input = sys.stdin.readline
INF = int(1e9)

# 정점의 개수 N, 간선의 개수 E
n, e = map(int, input().split())

# 인접 리스트로 그래프 표현 (양방향)
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 반드시 거쳐야 하는 두 정점
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
    
    return distance

# 1번에서 출발, v1과 v2를 거쳐 N번으로 가는 최단거리
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로1: 1 -> v1 -> v2 -> N
route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]

# 경로2: 1 -> v2 -> v1 -> N
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

# 두 경로 중 최소값
result = min(route1, route2)

# 경로가 존재하지 않는 경우
if result >= INF:
    print(-1)
else:
    print(result)

