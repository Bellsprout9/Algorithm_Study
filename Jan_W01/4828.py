import sys

sys.stdin = open('sample_input.txt')

T = int(input())        # 테스트케이스 수

for tc in range(1, T+1):        # 케이스별로 처리
    N = int(input())            # 테스트 케이스별로 첫 줄에 N = 케이스 별 입력 개수
    arr = list(map(int, input().split()))
    max_v = arr[0]  # 첫 원소를 최댓값으로 가정
    min_v = arr[0]  # 첫 원소를 최솟값으로 가정

    for i in range(1, N):       # N개의 양의 정수가 주어지면 인덱스가 N-1까지 있으므로
                                # 0번째 값은 최소 혹은 최대로 가정했으므로 1부터 진행
        if max_v < arr[i]:      # 가정한 값보다 큰 값이 왔을 경우
            max_v = arr[i]      # 해당 값을 최댓값으로 지정
        if min_v > arr[i]:      # 가정한 값보다 작은 값이 왔을 경우
            min_v = arr[i]      # 해당 값을 최솟값으로 지정
    print(f'#{tc} {max_v-min_v}')