import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline
n, m, v = map(int, input().split())

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬 (번호가 낮은 노드부터 방문하기 위해)
for i in range(1, n + 1):
    graph[i].sort()

# DFS 구현
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

# BFS 구현
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        curr = queue.popleft()
        print(curr, end=' ')
        for i in graph[curr]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

# 방문 기록 초기화 및 실행
visited_dfs = [False] * (n + 1)
dfs(v)
print()

visited_bfs = [False] * (n + 1)
bfs(v)
print()

