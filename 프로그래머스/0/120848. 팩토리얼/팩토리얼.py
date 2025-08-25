# while 반복문을 사용하여 n보다 작을 때의 조건이 깨질때까지 반복문을 돌림
# n과 비교할 수는 num, 카운트할 수는 answer
# n보다 작을 경우 카운트에 +1을 하고, num에 그 수를 곱함
# 반복문을 빠져 나올 경우 그 카운트(answer)를 반환
def solution(n):
    answer = 1
    num = 1
    while num*(answer+1) <= n:
        answer += 1
        num *= answer
    return answer