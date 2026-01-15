# 로봇 청소기
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 위 왼 아 오
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

maps[r][c] = 2
q = deque([(r, c, d)])
cnt = 1

while q:
    ci, cj, cd = q.popleft()
    cleaned = 0

    # 1. 현재 칸 주변에 청소할 곳이 있는지 판단
    for _ in range(4):
        # 1.1 왼쪽으로 90도씩 돌면서 확인
        cd = (cd + 3) % 4
        ni, nj = ci + di[cd], cj + dj[cd]

        # 1.2 청소 하러 전진 (q에 돌아간 방향으로 넣기)
        if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 0:
            cleaned = 1
            q.append((ni, nj, cd))
            maps[ni][nj] = 2
            cnt += 1
            break


    # 2. 청소할 곳이 없다면
    if not cleaned:
        # 2.1 cd 기준 후진하기
        nd = (cd + 2) % 4
        ni, nj = ci + di[nd], cj + dj[nd]

        if maps[ni][nj] != 1:
            q.append((ni, nj, cd))

        # 2.2 후진 안되면 끝
        else:
            break

print(cnt)
