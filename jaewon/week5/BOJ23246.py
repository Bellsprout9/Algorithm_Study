import sys

# 입력 받기
input = sys.stdin.readline
n = int(input())

athletes = []
for _ in range(n):
    # b: 선수 번호, p, q, r: 세 종목의 순위
    b, p, q, r = map(int, input().split())
    # 순위의 곱, 순위의 합, 선수 번호 순으로 저장
    athletes.append((p * q * r, p + q + r, b))

# 1. 곱이 작은 순
# 2. 곱이 같다면 합이 작은 순
# 3. 곱과 합이 모두 같다면 번호가 작은 순
athletes.sort()

# 상위 3명의 선수 번호 출력
for i in range(3):
    print(athletes[i][2], end=' ')
print()

