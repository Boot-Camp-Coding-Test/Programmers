def solution(n):
    answer = 0
    
    # ['1','2','3'] 형태로 반환됨
    splitted_list = list(str(n))
    
    # 차례대로 int형으로 바꿔주고 더해주기
    for i in splitted_list :
        answer+=int(i)

    return answer
