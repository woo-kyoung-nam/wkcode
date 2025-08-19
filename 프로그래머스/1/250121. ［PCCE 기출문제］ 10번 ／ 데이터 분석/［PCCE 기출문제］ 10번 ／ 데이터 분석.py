# 1. data에서 ext값이 val_ext보다 작은 값만 추출
# 2. sort_by에서 remain값을 기준으로 오름차순 정렬

def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {'code':0,'date':1,'maximum':2,'remain':3}   # 컬럼 정보를 담음
    for i in data:
        if i[dic[ext]] < val_ext:          # ext이 val_ext보다 작은 값들을 적재
            answer.append(i)
    answer.sort(key=lambda x : x[dic[sort_by]])      
    return answer
    