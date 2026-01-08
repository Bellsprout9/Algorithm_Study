# 최소비용 구하기
import heapq
import sys

N = int(input())
M = int(input())

graph = {v:[] for v in range(N+1)}
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s, e = map(int, input().split())

dist = [float('inf')] * (N+1)
dist[s] = 0

q = []

heapq.heappush(q, (0, s))

while q:
    curr_cost, curr_node = heapq.heappop(q)

    if dist[curr_node] < curr_cost:
        continue

    for next_node, next_cost in graph[curr_node]:
        cost = curr_cost + next_cost

        if dist[next_node] > cost:
            dist[next_node] = cost
            heapq.heappush(q, (cost, next_node))

print(dist[e])