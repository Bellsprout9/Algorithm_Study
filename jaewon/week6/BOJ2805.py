import sys

# 나무 자르기 - 이진 탐색
input = sys.stdin.readline

n, m = map(int, input().split())  # 나무의 수, 필요한 나무 길이
trees = list(map(int, input().split()))

def cut_trees(height):
    """주어진 높이로 잘랐을 때 가져갈 수 있는 나무의 총 길이"""
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

# 이진 탐색으로 최대 높이 찾기
left, right = 0, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    
    # mid 높이로 잘랐을 때 가져갈 수 있는 나무 길이
    wood = cut_trees(mid)
    
    if wood >= m:  # 필요한 길이보다 많이 가져갈 수 있으면
        result = mid  # 현재 높이를 저장
        left = mid + 1  # 더 높은 높이로 시도
    else:  # 필요한 길이보다 적게 가져가면
        right = mid - 1  # 더 낮은 높이로 시도

print(result)

