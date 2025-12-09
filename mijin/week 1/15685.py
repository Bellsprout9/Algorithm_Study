# 백준 - 드래곤 커브
N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * 101 for _ in range(101)]

# 우 상 좌 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in curves:
    visited[y][x] = 1

    directions = [d]

    for _ in range(g):
        for dir in reversed(directions):
            directions.append((dir + 1) % 4)

    nx, ny = x, y
    for dir in directions:
        nx += dx[dir]
        ny += dy[dir]
        visited[ny][nx] = 1

result = 0
for y in range(100):
    for x in range(100):
        if visited[y][x] and visited[y][x+1] and visited[y+1][x] and visited[y+1][x+1]:
            result += 1

print(result)