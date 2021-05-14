        # 한문제 통과 안 됨....
        # 그렇다고 첫번째 조건문을 그냥 len()으로 고치면 런타임 초과됨
        
def solution(s):
    if len(s)%2==0:
        return s[round(len(s)/2)-1]+s[round(len(s)/2)-1]
    else:
        return s[round(len(s)/2)]
        
