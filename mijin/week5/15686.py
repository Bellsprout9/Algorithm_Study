# 치킨 배달
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

# 집, 치킨집 좌표 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 백트래킹으로 M개의 치킨집 선택하면서 최소값 계산
min_dist = float('inf')
selected = []

# 해당 치킨 거리 계산
def calc_dist():
    total = 0
    for hx, hy in house:
        dist = float('inf')
        for cx, cy in selected:
            d = abs(hx - cx) + abs(hy - cy)
            if d < dist:
                dist = d
        total += dist

        if total >= min_dist:
            return total
    return total

def backtrack(start, cnt):
    global min_dist

    # M개 다 선택한 경우
    if cnt == M:
        min_dist = min(min_dist, calc_dist())
        return

    for idx in range(start, len(chicken) - (M - cnt) + 1):
        selected.append(chicken[idx])
        backtrack(idx + 1, cnt + 1)
        selected.pop()

backtrack(0,0)
print(min_dist)
