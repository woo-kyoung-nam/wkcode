# 97~123 : a~z의 아스키 코드
# skip에 있는 문자열을 제외한 알파벳 목록을 구한다. 이를 skipped 라 칭한다.
# s를 순회하며 skipped에서 현재 알파벳의 인덱스를 찾아 index 만큼 더해준다. 
# 이 때, skipped 의 총 길이를 초과한다면 그 나머지를 구한다.
# result에 2에서 구한 인덱스의 알파벳을 더한다.
def solution(s, skip, index):
    skipped = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    res = ""
    for i in s:
        res += skipped[(skipped.index(i) + index) % len(skipped)]
    return res