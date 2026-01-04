# 로봇청소기

# 현재 칸이 청소된 경우

# 주변 4칸 탐색 

# 청소 가능 -> 90도 회전 후 청소 -> 반복
# 청소 불가능 & 후진 가능 -> 후진하고 반복
# 청소 불가능 & 후진 불가능 -> 작동 멈춤 

# 현재 칸이 청소된 경우
# 주변 4칸 탐색

# 청소 가능 -> 90도 회전 후 청소 -> 반복
# 청소 불가능 & 후진 가능 -> 후진하고 반복
# 청소 불가능 & 후진 불가능 -> 작동 멈춤 

import sys
input = sys.stdin.readline

# 입력 
N, M = map(int, input().split())
cr, cc, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 청소 횟수 
clean = 0

# 방향: 0=북, 1=동, 2=남, 3=서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


while True:

    # 현재 위치 청소 가능 
    if arr[cr][cc] == 0:
        arr[cr][cc] = 2
        clean += 1
    
    # 현재 위치 청소 불가능하면 4방향 탐색 
    turn = False
    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            cr, cc = nr, nc 
            
            # 회전 해서 청소 가능 칸 찾으면 회전 그만
            turn = True 
            break
    
    # 전진하면 아래 코드 무시하고 다음 루프
    if turn:
        continue 
    
    # 4방향 중 청소할 곳 없음 -> 후진 
    br, bc = cr - dr[d], cc - dc[d]
    if 0<=br<N and 0<=bc<M and arr[br][bc] != 1:
        cr, cc = br, bc
        continue 
    
    # 후진도 불가능하면 while True문 빠져나가기 
    break 
print(clean)