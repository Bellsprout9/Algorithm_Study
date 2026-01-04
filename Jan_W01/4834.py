# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

import sys

sys.stdin = open('sample_input.txt')
T = int(input())


for test_case in range(1, T+1):
    N = int(input())
    string = str(input())
    arr = list(string)

    # 숫자카드와 개수를 각각 key, value로 담을 딕셔너리
    dic = {}

    # 딕셔너리 업데이트
    for item in arr:                # 리스트에 담긴 숫자카드 중에서
        if item not in dic.keys():  # 숫자카드가 딕셔너리의 키목록에 없으면
            dic[item] = 1           # value = 1 로 딕셔너리에 추가
        else:
            dic[item] += 1          # 딕셔너리에 있는 카드면 기존 개수(value)에서 +1

    max_num = dic[arr[0]]           # 초기 최대 장 수 가정
    max_key = arr[0]                # 초기 최대 숫자카드 가정

    for key, value in dic.items():
        key = int(key)              # key와 value를 int로 조정
        value = int(value)

        if value > max_num:         # 가정된 장 수보다 큰 장 수가 있으면
            max_num = value         # 최대 장수를 업데이트
            max_key = key           # 최대 숫자카드 업데이트
        elif value == max_num and key > int(max_key):       # 만약 같은 장 수가 나오면
            max_key = key                                   # 큰 값으로 업데이트

    print(f'#{test_case} {max_key} {max_num}')