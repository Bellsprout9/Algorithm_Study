# 용액 합성하기
N = int(input())
A = list(map(int, input().split()))

A.sort()

left, right = 0, N-1
answer = float('inf')

while left < right:
    mid = A[left] + A[right]

    if abs(mid) < abs(answer):
        answer = mid

    if mid < 0:
        left += 1

    else:
        right -= 1

print(answer)