import sys
from collections import deque

# 유기농 배추 - BFS/DFS로 연결된 배추 영역 찾기
input = sys.stdin.readline

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    field[x][y] = 0  # 방문 처리
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 배추가 있으면 방문
            if field[nx][ny] == 1:
                field[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))

# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추 개수
    
    # 밭 초기화
    field = [[0] * m for _ in range(n)]
    
    # 배추 위치 입력
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    # 필요한 배추흰지렁이 수
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
    
    print(count)

