def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]  # 최소값부터 최댓값의 범위를 설정
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])