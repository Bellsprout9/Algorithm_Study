# 옥상정원 꾸미기
N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
answer = 0

for idx, building in enumerate(buildings):
    while stack and stack[-1] <= building:
        stack.pop()

    answer += len(stack)
    stack.append(building)

print(answer)