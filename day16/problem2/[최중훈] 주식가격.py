from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    for _ in range(len(prices)):
        current = prices.popleft()
        cnt = 0
        for future in prices:
            cnt += 1
            if current > future:
                break
        answer.append(cnt)
    
    return answer
