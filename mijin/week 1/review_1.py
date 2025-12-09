# 킬-어시스트 맞추기
def solution(kills, assists):
    n = len(kills)

    # 1. 일단 1차 목표
    max_kill = max(kills)
    max_assist = max(assists)

    # 2. 일단 킬수는 맞춰야 되니까
    # 내가 해야할 킬 수
    kill_diff = [max_kill - curr_kill for curr_kill in kills]
    sum_kill_diff = sum(kill_diff)

    # 3. 주어진 킬을 하면서 얻을 수 있는 최대 어시스트 저장하기
    assist_additional = []
    for i in range(n):
        # 내가 얻을 수 있는 어시 = 이 게임에서의 총 킬수 - 내가 한 킬 수
        possible_assist = sum_kill_diff - kill_diff[i]
        assist_additional.append(assists[i] + possible_assist)

    # 4. 근데 아직!! 어시가 다 안채워졌을 수 있으니까 그거 확인
    extra_assist = 0
    for a in assist_additional:
        # 목표 어시 - 현재 가능한 최대 어시 > 0 이라는 건 아직 어시를 채워야된다는 것..
        if max_assist - a > 0:
            extra_assist = max(extra_assist, max_assist - a)

    # 5. 후.. 이제 진짜 마지막 계산
    # 어시스트는 어차피 max값이 최종임
    # 근데 어시스트 부족할 경우 kill은 늘어나야 되니까 kill에는 보정값 추가
    final_kill = max_kill + extra_assist
    final_assist = max_assist

    return [final_kill, final_assist]

print(solution([4,2,3], [1,0,2]))
print(solution([1,1,1], [0,1,0]))
print(solution([1000], [0]))