import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())

# 좌표 저장
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

# x좌표 기준 오름차순, x좌표가 같으면 y좌표 기준 오름차순 정렬
# 파이썬의 sort는 기본적으로 튜플/리스트의 각 요소를 순서대로 비교함
points.sort(key=lambda x: (x[0], x[1]))

# 결과 출력
for p in points:
    print(f"{p[0]} {p[1]}")

