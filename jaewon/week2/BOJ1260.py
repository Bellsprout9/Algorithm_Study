from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 인접 리스트를 정렬해 번호가 작은 노드부터 방문하도록 설정
for i in range(1, n + 1):
    graph[i].sort()

# 방문 여부 초기화
visited = [False] * (n + 1)

# DFS
dfs(graph, v, visited)
print()

# 방문 여부 초기화
visited = [False] * (n + 1)

# BFS
bfs(graph, v, visited)

