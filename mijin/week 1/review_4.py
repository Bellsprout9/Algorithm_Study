# 문자열로 트리 만들기
from collections import defaultdict

def solution(names, queries):
    # 1. name의 모든 prefix 카운트
    prefix_count = defaultdict(int)

    for name in names:
        prefix = ""
        for ch in name:
            prefix += ch
            prefix_count[prefix] += 1

    # 2. 각 query에 대해 prefix별 개수 합산
    answer = []

    for q in queries:
        prefix = ""
        total = 0
        for ch in q:
            prefix += ch
            total += prefix_count.get(prefix, 0)
        answer.append(total)

    return answer