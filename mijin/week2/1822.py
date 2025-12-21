# 차집합
nA, nB = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

answer = []

# 이게 a랑 b 앞에서부터 순회하면서 a가 크면 b의 index 늘리고 이런식으로 하는거 같은데
# 근데 같은걸 저장할 수는 있는데 다른걸 어떻게 판단하지?

i, j = 0, 0

while i < nA and j < nB:
    if A[i] < B[j]:
        answer.append(A[i])
        i += 1

    elif A[i] > B[j]:
        j += 1

    else:
        i += 1
        j += 1

if j == nB:
    answer.extend(A[i:])

if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(*answer)