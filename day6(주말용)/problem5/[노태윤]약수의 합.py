def solution(n):
    # False 면 약수 X / True 면 약수 O
    tf_list = [False] * (n+1)

    for i in range(1,n+1) :
      
        # 이미 약수라고 지정된 값이 있으면 그냥 continue
        if tf_list[i] == True :
            continue
        
        # a : remainder / b : 나눴을 때 나오는 값
        a = n%i
        b = n//i
        
        # 만약 나누어 떨어진다면 아래 코드 실행
        if a == 0 :
            tf_list[i] = True
            tf_list[b] = True

    answer = 0
    
    # enumerate 시키면 (0,False),(1,True),(2,True)... 이런 식으로 됨
    for c,d in enumerate(tf_list) :
        
        # 약수가 맞다면 계속해서 더해주기
        if d==True :
            answer+=c
    return answer
