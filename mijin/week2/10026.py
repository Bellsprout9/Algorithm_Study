# 적녹색약
from collections import deque

N = int(input())
painting = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

cnt1 = 0
cnt2 = 0

# 1. 일반인 계산
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q = deque([(i, j, painting[i][j])])
            visited[i][j] = 1
            cnt1 += 1

            while q:
                ci, cj, cc = q.popleft()

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]

                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        if cc == painting[ni][nj] :
                            q.append((ni, nj, painting[ni][nj]))
                            visited[ni][nj] = 1


visited = [[0] * N for _ in range(N)]

# 2. 색약 계산
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q = deque([(i, j, painting[i][j])])
            visited[i][j] = 1
            cnt2 += 1

            while q:
                ci, cj, cc = q.popleft()

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]

                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        # 1. 적 or 녹일 경우
                        if cc in ('R', 'G') and painting[ni][nj] in ('R', 'G'):
                            q.append((ni, nj, painting[ni][nj]))
                            visited[ni][nj] = 1

                        # 2. B일 경우
                        elif cc == painting[ni][nj]:
                            q.append((ni, nj, painting[ni][nj]))
                            visited[ni][nj] = 1

print(cnt1, cnt2)