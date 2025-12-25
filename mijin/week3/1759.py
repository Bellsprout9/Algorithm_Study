# 암호 만들기
L, C = map(int, input().split())

strings = list(input().split())
strings.sort()

arr = [''] * L
vowels = {'a','e','i','o','u'}

def backtrack(depth, start):
    if depth == L:
        v_cnt = 0
        for char in arr:
            if char in vowels:
                v_cnt += 1

        if v_cnt >= 1 and L - v_cnt >= 2:
            print(''.join(arr))
        return

    for idx in range(start, C):
        arr[depth] = strings[idx]
        backtrack(depth + 1, idx+1)

backtrack(0, 0)

