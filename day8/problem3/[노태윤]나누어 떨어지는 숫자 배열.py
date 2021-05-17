def solution(arr, divisor):
    answer = []
    
    # arr 한번씩 돌기
    for i in arr :
      
        # divisor 로 나누어 떨어진다면 answer 에 append
        if i % divisor == 0 :
            answer.append(i)
    
    # 만약 append 된게 하나도 없다면 [-1] 반환
    if len(answer) == 0 :
        return [-1]
    
    # answer list 오름차순으로 정렬
    answer.sort()
    return answer
