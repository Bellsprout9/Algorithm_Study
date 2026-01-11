import sys

# 입력 받기
input = sys.stdin.readline
n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 쌍의 수

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

def dfs(v):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(i)

dfs(1) # 1번 컴퓨터부터 시작
print(count)

