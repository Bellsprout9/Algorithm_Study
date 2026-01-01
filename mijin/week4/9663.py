# N-Queen -> pypy만 맞음 ㅋㅋ ;;
N = int(input())

selected = [0] * N
cnt = 0

def is_safe(col, row):
    for prev_col in range(col):
        # 1. 같은 행에 없는지
        if selected[prev_col] == row:
            return False

        # 2. 대각선에 없는지 -> 기울기
        if abs(prev_col - col) == abs(selected[prev_col] - row):
            return False

    return True

def backtrack(col):
    global cnt

    if col == N:
        cnt += 1
        return

    for row in range(N):
        if is_safe(col, row):
            selected[col] = row
            backtrack(col + 1)

backtrack(0)
print(cnt)
