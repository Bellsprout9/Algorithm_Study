# 절댓값 힙
import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))

    else:
        if hq:
            abs_y, y = heapq.heappop(hq)
            print(y)
        else:
            print(0)