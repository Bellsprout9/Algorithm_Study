# 물대기
N = int(input())
W = [int(input()) for _ in range(N)]
costs = [list(map(int, input().split())) for _ in range(N)]

selected = [0] * N
# 해당 노드를 mst에 붙이기 위해 드는 최소 비용
key = W[:]
answer = 0

for _ in range(N):
    u, min_val = -1, float('inf')

    # 아직 방문 안한 정점 찾기
    for i in range(N):
        if not selected[i] and key[i] < min_val:
            min_val= key[i]
            u = i

    # 갈수 없는 정점이 없으면 종료
    if u == -1:
        break

    # u를 mst에 넣기
    selected[u] = 1
    answer += key[u]

    # u와 연결된 모든 정점에 대해 key 갱신
    for v in range(N):
        if not selected[v] and costs[u][v] < key[v]:
            key[v] = costs[u][v]

print(answer)

