# 가장 긴 짝수 연속한 부분 수역
N, K = map(int, input().split())
S = list(map(int, input().split()))

left = 0
right = 0

answer = 0
remove = 0
cnt = 0

while left <= right and right < N:
    if S[right] % 2 == 0:
        cnt += 1
    else:
        remove += 1
    right += 1

    while remove > K:
        if S[left] % 2 == 0:
            cnt -= 1
        else:
            remove -= 1
        left += 1
    answer = max(answer, cnt)

print(answer)

# for i in range(N):
#     print(even_cnt, S[i])
#     # 홀수라면
#     if S[i] % 2 == 1:
#         if cnt != 0:
#             even_cnt.append(cnt)
#             cnt = 0
#         even_cnt.append(0)
#     # 짝수라면
#     else:
#         cnt += 1

# # 짝수가 없다면 종료
# if sum(even_cnt) == 0:
#     print(0)
#
# else:
#     # even_cnt를 투포인터로 돌면서 누적합이 제일 큰거 찾기
#     left = 0
#     while even_cnt[left] != 0:
#         left += 1
#
#     right = left + 1
#
#     # 근데 짝수가 한개가 끝이면 어쩌지
#     answer = even_cnt[left]
#     print(answer)
#     curr_sum = even_cnt[left]
#     remove = 0
#
#     while left < right and right < len(even_cnt):
#         if even_cnt[right] == 0:
#             remove += 1
#
#             if remove > K:
#                 answer = max(answer, curr_sum)
#
#                 while even_cnt[left] != 0 and left < N-1:
#                     left += 1
#
#                 curr_sum = even_cnt[left]
#                 right = left + 1
#
#             right += 1
#
#         else:
#             curr_sum += even_cnt[right]
#             right += 1
#
#     print(answer)