def solution(phone_number):
    
    # 마지막 4개 번호 반환
    last_four = phone_number[-4:]
    
    # 마지막 4 자리 제외한 길이 반환
    lengths = len(phone_number) - 4
    
    # * 곱하기 lengths 한 만큼 반환
    symbol = '*' * lengths
    answer = symbol + last_four
    return answer
