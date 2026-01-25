import sys
import heapq

# 녹색 옷 입은 애가 젤다지? - 2D 그리드에서 다익스트라
input = sys.stdin.readline
INF = int(1e9)

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, cave):
    # 최소 비용 테이블
    distance = [[INF] * n for _ in range(n)]
    
    # 우선순위 큐 (비용, x, y)
    queue = []
    heapq.heappush(queue, (cave[0][0], 0, 0))
    distance[0][0] = cave[0][0]
    
    while queue:
        cost, x, y = heapq.heappop(queue)
        
        # 이미 처리된 칸이라면 무시
        if distance[x][y] < cost:
            continue
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 새로운 비용 계산
            new_cost = cost + cave[nx][ny]
            
            # 더 적은 비용이라면 업데이트
            if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                heapq.heappush(queue, (new_cost, nx, ny))
    
    return distance[n-1][n-1]

# 테스트 케이스 처리
problem_num = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    # 동굴 정보 입력
    cave = [list(map(int, input().split())) for _ in range(n)]
    
    # 최소 비용 계산
    result = dijkstra(n, cave)
    
    print(f"Problem {problem_num}: {result}")
    problem_num += 1

