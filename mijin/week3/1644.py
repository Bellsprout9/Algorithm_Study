# 소수의 연속합
import math
N = int(input())

if N < 2:
    print(0)
else:
    # 1. N 이하의 소수 배열 생성
    nums = [1] * (N + 1)
    nums[0] = 0
    nums[1] = 0

    for i in range(2, int(math.sqrt(N) + 1)):
        if nums[i] == 1:
            j = 2
            while i * j <= N:
                nums[i * j] = 0
                j += 1

    prime_nums = [ i for i in range(2, N+1) if nums[i] == 1 ]

    # 2. 소수 배열을 양끝에서 탐색하면서 N 찾기
    prime_len = len(prime_nums)
    cnt = 0

    left, right = 0, 0
    sum_val = prime_nums[0]

    while left <= right:
        if sum_val == N:
            cnt += 1
            # sum_val -= prime_nums[left]
            # left += 1

        if sum_val < N:
            right += 1
            if right >= prime_len:
                break
            sum_val += prime_nums[right]

        else:
            sum_val -= prime_nums[left]
            left += 1
            if left >= prime_len:
                break

    print(cnt)