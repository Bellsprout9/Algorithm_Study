# 콩 심기
def solution(beans, cards):
    # 1. 전처리: 콩 이름 -> 인덱스, 필요 개수, 점수 매핑
    name_to_idx = {}
    bean_need = []
    bean_score = []

    for s in beans:
        name, need, score = s.split()
        name_to_idx[name] = len(bean_need)
        bean_need.append(int(need))
        bean_score.append(int(score))

    # 2. cards를 숫자 인덱스 배열로 변환
    card_idx = [name_to_idx[name] for name in cards]
    n = len(card_idx)

    # 계산된 결과 저장
    memo = {}

    def dp(i, t1, r1, t2, r2):
        """
        i: 현재 처리할 카드 인덱스
        t1, t2: 밭1, 밭2에 심긴 콩 종류 (비어있으면 -1)
        r1, r2: 밭1, 밭2에 심긴 콩의 현재 개수
        """
        # 1. 종료 조건: 모든 카드를 다 썼을 때
        if i == n:
            return 0

        # 2. 이미 계산해본 상황인지 확인 -> 그렇다면? 그만 탐색
        state = (i, t1, r1, t2, r2)
        if state in memo:
            return memo[state]

        # 3. 로직 수행
        b = card_idx[i]
        need_b = bean_need[b]
        score_b = bean_score[b]

        best = 0

        # --- 선택지 1: 밭1에 심기 (비어있거나 같은 콩일 때) ---
        if t1 == -1 or t1 == b:
            new_t1 = b
            new_r1 = r1 + 1 if t1 == b else 1
            gain = 0

            # 수확 조건 달성
            if new_r1 == need_b:
                gain = score_b
                new_r1 = 0

            val = gain + dp(i + 1, new_t1, new_r1, t2, r2)
            best = max(best, val)

        # --- 선택지 2: 밭2에 심기 (비어있거나 같은 콩일 때) ---
        if t2 == -1 or t2 == b:
            new_t2 = b
            new_r2 = r2 + 1 if t2 == b else 1
            gain = 0

            if new_r2 == need_b:
                gain = score_b
                new_r2 = 0

            val = gain + dp(i + 1, t1, r1, new_t2, new_r2)
            best = max(best, val)

        # --- 선택지 3: 둘 다 꽉 차서 하나를 갈아엎어야 할 때 ---
        # (t1, t2가 모두 -1이 아니고, 심으려는 콩 b와도 다를 때)
        if t1 != -1 and t1 != b and t2 != -1 and t2 != b:
            # 3-1) 밭1 갈아엎고 심기
            val1 = 0 + dp(i + 1, b, 1, t2, r2)

            # 3-2) 밭2 갈아엎고 심기
            val2 = 0 + dp(i + 1, t1, r1, b, 1)

            best = max(best, val1, val2)

        # 4. 계산된 최적해를 기록
        memo[state] = best
        return best

    return dp(0, -1, 0, -1, 0)