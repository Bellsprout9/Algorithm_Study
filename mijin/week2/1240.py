# 노드 사이의 거리
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    s, e, w = map(int, input().split())

    graph[s].append((e,w))
    graph[e].append((s,w))

for i in range(M):
    node1, node2 = map(int, input().split())

    stack = [(node1, 0)]
    visited = [0] * (N + 1)
    visited[node1] = 1

    while stack:
        curr_node, curr_dist = stack.pop()

        if curr_node == node2:
            print(curr_dist)
            break

        for next_node, next_dist in graph[curr_node]:
            if not visited[next_node]:
                stack.append((next_node, curr_dist + next_dist))
                visited[next_node] = 1
