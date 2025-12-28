# 퇴사 2
import sys
input = sys.stdin.readline

N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * (N + 1)

for i in range(N):
    if i + counsel[i][0] <= N:
        DP[i + counsel[i][0]] = max(DP[i + counsel[i][0]], DP[i] + counsel[i][1])
    DP[i+1] = max(DP[i], DP[i+1])

print(max(DP))
# print(DP[N]) -> 이것도 맞음 지피티가 틀리다고 했는데 제출하니까 맞음 ㅡㅡ