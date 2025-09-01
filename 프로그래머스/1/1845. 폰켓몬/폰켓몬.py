# 포켓몬 중 n/2마리 가져갈수있음 (ex, 배열의 길이가 전체 4이면 2마리만 가질수있음)
# 같은 종류의 포켓몬은 같은 번호를 가지고 있음
# 가장 많은 종류의 폰켓몬을 선택하고, 그때의 폰켓몬 종류 번호의 개수를 return
# Q : 서로 다른 수를 가져오고, 중복처리?  
# https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8F%B0%EC%BC%93%EB%AA%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python

def solution(nums):
    answer = len(set(nums))
    if answer > len(nums)/2:
        return len(nums)/2
    return answer    
