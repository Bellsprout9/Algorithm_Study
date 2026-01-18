import sys
from collections import deque

# 토마토 - BFS로 최소 시간 구하기
input = sys.stdin.readline

m, n = map(int, input().split())  # 가로, 세로
box = [list(map(int, input().split())) for _ in range(n)]

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토의 위치를 모두 큐에 넣기
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 익지 않은 토마토를 발견하면
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

bfs()

# 결과 확인
max_day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:  # 익지 않은 토마토가 있으면
            print(-1)
            exit()
        max_day = max(max_day, box[i][j])

# 처음부터 1이었으므로 실제 걸린 시간은 -1
print(max_day - 1)

