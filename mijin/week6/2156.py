# 포도주 시식
N = int(input())
wines = [int(input()) for _ in range(N)]

if N == 1:
    print(wines[0])

elif N == 2:
    print(wines[0] + wines[1])

else:
    DP = [-1] * N
    DP[0] = wines[0]
    DP[1] = wines[0] + wines[1]
    DP[2] = max(DP[1], wines[0] + wines[2], wines[1] + wines[2])

    for i in range(3, N):
        # 현재 안마시기, 이전거 안마시기, 이전전거 안마시기
        DP[i] = max(DP[i-1], DP[i-2] + wines[i], DP[i-3] + wines[i-1] + wines[i])

    print(DP[N-1])
