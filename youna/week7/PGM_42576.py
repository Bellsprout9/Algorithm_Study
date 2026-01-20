def solution(participant, completion):
    hash_dict = {}
    
    # 참가자 이름 카운트
    for name in participant:
        hash_dict[name] = hash_dict.get(name, 0) + 1
    
    # 완주자 이름 감소
    for name in completion:
        hash_dict[name] -= 1
    
    # 값이 1인 사람이 완주 못한 사람
    for name, count in hash_dict.items():
        if count == 1:
            return name