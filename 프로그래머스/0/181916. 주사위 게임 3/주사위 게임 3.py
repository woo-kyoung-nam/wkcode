def solution(a, b, c, d):
    # 리스트로 생성 후, 오름차순 정렬
    num = sorted([a,b,c,d])
    
    # 1. 네 주사위 숫자가 같음
    if num[0] == num[1] == num[2] == num[3]:
        return 1111*num[0]
    
    # 2. 세 개의 숫자가 같음 (4441,1444)
    if num[0] == num[2] or num[1] == num[3]:
        p = num[1]   # 조건문에 공통으로 표현된값
        q = num[3] if num[3] != num[1] else num[0]
        return (10*p+q)**2
    
    # 3. 두 개씩 숫자가 같음(3366, 6633)
    if num[0] == num[1] and num[2] == num[3]:
        p = num[0]
        q = num[2]
        return (p+q) * abs(p-q)
    
    # 4. 두 개의 주사위만 같은 숫자 (2256, 2445, 2355)
    if num[0] == num[1]:
        return num[2] * num[3]
    elif num[1] == num[2]:
        return num[0] * num[3]
    elif num[2] == num[3]:
        return num[0] * num[1]
    
    # 5. 네 개의 주사위 모두 다를 때 가장 작은 숫자
    return num[0]