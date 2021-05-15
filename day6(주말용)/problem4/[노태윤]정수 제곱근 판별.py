def solution(n):
    
    # 제곱근 구하기
    sqrt_value = n**0.5
    
    # 만약 끝자리가 '0' 이면 / 나누어 떨어진다면 아래 실행
    if str(sqrt_value)[-1] == '0' :
        return int((sqrt_value+1)**2)
    
    # 그 외에는 -1 반환
    else :
        return -1
