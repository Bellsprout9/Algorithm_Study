# 수 묶기
N = int(input())
arr = [int(input()) for _ in range(N)]

# 아무 수도 묶지 않았을 경우를 기준
sum_val = sum(arr)

if N == 1:
    print(sum_val)
else:
    arr.sort()
    multiple_val = 0

    # arr를 돌면서 0과 양수가 만날때, 음수와 양수가 만날때 빼고는 다 곱하기
    i = 0
    # 음수, 0까지 계산
    while i < N-1 and arr[i+1] <= 0:
        multiple_val += (arr[i] * arr[i + 1])
        i += 2

    if i < N and arr[i] <= 0:
        multiple_val += arr[i]
        i += 1

    # 양수일 때 계산 (1은 곱하면 손해)
    j = N-1
    while i < j and arr[j-1] > 1:
        multiple_val += (arr[j] * arr[j - 1])
        j -= 2

    # 남은 애들 정리
    for k in range(i, j + 1):
        multiple_val += arr[k]

    print(multiple_val)