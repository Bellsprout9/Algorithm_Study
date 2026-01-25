import sys
import heapq

# 파티 - 왕복 최단거리 (다익스트라 여러 번 수행)
input = sys.stdin.readline
INF = int(1e9)

# N: 학생 수(정점), M: 도로 수(간선), X: 파티 장소
n, m, x = map(int, input().split())

# 정방향 그래프와 역방향 그래프 생성
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())  # a->b 소요시간 t
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))  # 역방향

def dijkstra(start, g):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for next_node, cost in g[now]:
            new_cost = dist + cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
    
    return distance

# X에서 각 마을로 가는 최단거리 (돌아가는 거리)
go_home = dijkstra(x, graph)

# 각 마을에서 X로 가는 최단거리 (가는 거리)
# 역방향 그래프에서 X를 시작점으로 다익스트라
come_to_party = dijkstra(x, reverse_graph)

# 각 학생의 왕복 시간 중 최댓값
max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, go_home[i] + come_to_party[i])

print(max_time)

