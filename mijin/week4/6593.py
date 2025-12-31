# 상범 빌딩
from collections import deque

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    buildings = []

    for _ in range(L):
        floor = []
        for _ in range(R):
            floor.append(list(input()))
        buildings.append(floor)

        input()

    # S, E 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if buildings[i][j][k] == 'S':
                    start = (i, j, k)

                if buildings[i][j][k] == 'E':
                    ei, ej, ek = i, j, k

    # bfs로 3차원 탐색
    q = deque([start])
    si, sj, sk = start
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    visited[si][sj][sk] = 0

    di = [0, 0, 0, 0, -1, 1]
    dj = [0, 0, -1, 1, 0, 0]
    dk = [-1, 1, 0, 0, 0, 0]

    found = 0

    while q:
        ci, cj, ck = q.popleft()

        if (ci, cj, ck) == (ei, ej, ek):
            sec = visited[ci][cj][ck]
            found = 1
            break

        # 상하좌우남북 탐색
        for d in range(6):
            ni, nj, nk = ci + di[d], cj + dj[d], ck + dk[d]

            # 다음 좌표가 범위 내에 있고, 방문하지 않았고, .이라면 q에 넣기
            if 0 <= ni < L and 0 <= nj < R and 0 <= nk < C:
                if visited[ni][nj][nk] == -1 and buildings[ni][nj][nk] in ('.', 'E'):
                    q.append((ni, nj, nk))
                    visited[ni][nj][nk] = visited[ci][cj][ck] + 1

    if found:
        print(f'Escaped in {sec} minute(s).')
    else:
        print('Trapped!')
