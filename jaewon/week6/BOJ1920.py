import sys

# 수 찾기 - 이진 탐색
input = sys.stdin.readline

# N개의 정수 입력
n = int(input())
a = list(map(int, input().split()))
a.sort()  # 이진 탐색을 위해 정렬

# M개의 정수 입력
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

# 각 타겟에 대해 존재 여부 확인
for target in targets:
    print(binary_search(a, target))

