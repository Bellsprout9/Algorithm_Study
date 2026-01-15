# 감소하는 수
N = int(input())
nums = []

def dfs(last_digit, curr_num):
    nums.append(curr_num)

    # 여기서 마지막 자리수보다 작은걸로 채우니까 감소하는 수가 보장됨
    for next_digit in range(last_digit):
        dfs(next_digit, curr_num * 10 + next_digit)

# 0에서 9까지 한 자리씩 넣으면서
for start_digit in range(10):
    dfs(start_digit, start_digit)

nums.sort()

if N >= len(nums):
    print(-1)
else:
    print(nums[N])