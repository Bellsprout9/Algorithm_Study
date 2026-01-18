import sys
sys.setrecursionlimit(10000)

# 연결 요소의 개수 - DFS
input = sys.stdin.readline

n, m = map(int, input().split())  # 정점의 개수, 간선의 개수

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

