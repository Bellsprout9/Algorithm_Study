# 안전 영역
from collections import deque

N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
for i in range(N):
    max_height = max(max_height, max(heights[i]))

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

answer = 0
for h in range(101):
    if h > max_height:
        break

    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if heights[i][j] > h and not visited[i][j]:
                cnt += 1

                q = deque([(i,j)])
                visited[i][j] = 1

                while q:
                    ci, cj = q.popleft()

                    for d in range(4):
                        ni, nj = ci + di[d], cj + dj[d]

                        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and heights[ni][nj] > h:
                            q.append((ni, nj))
                            visited[ni][nj] = 1

                answer = max(answer, cnt)


print(answer)
