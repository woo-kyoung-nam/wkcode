def solution(price):
    if price >= 100000:
        if price >= 500000:
            price *= 0.8
        elif price >= 300000:
            price *= 0.9
        else:
            price *= 0.95
    return int(price)