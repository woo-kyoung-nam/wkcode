# Key = 의상의 종류
def solution(clothes):
    answer = 1
    closets = {}
    
    for _,k in clothes:               #의상의 이름은 보지않고, 의상의 종류만 봄
        if k in closets:
            closets[k] += 1
        else:
            closets[k] = 1
    
    for k in closets:
        answer *= closets[k] + 1
        
    return answer -1 


# 파이썬의 대표적인 해시 자료구조인 딕셔너리를 이용했습니다. 딕셔너리 형태로 closet을 선언하고, 반복문을 통해 주어진 clothes를 살펴봅니다. clothes의 첫번째 열은 옷의 이름, 두번째 열은 옷의 종류인데요. 옷의 종류를 closet의 Key로 보고 해당 Key가 딕셔너리에 없다면 closet[k] = 1, 있다면 closet[k] += 1을 실행합니다. 즉, 종류별로 옷이 몇 개 있는지 파악하는 것이죠!

# 이제 종류별로 옷들을 조합할 수 있는 경우의 수를 생각해보아야겠죠? 만약 모자가 2개(h1,h2), 상의가 2개(u1,u2)라면 몇 가지 조합이 가능할까요? [h1, h2, u1, u2, h1+u1, h1+u2, h2+u1, h2+u2] --> 총 8가지가 나옵니다. 이런 식으로 여러 경우들을 생각해보았을 때, 우리는 일반항을 (x+1) * (y+1) - 1로 도출할 수 있습니다! 이 일반항에 따라 answer을 구하여 return하면 되겠습니다.